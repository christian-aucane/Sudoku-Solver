import argparse
import json

import plotly.graph_objs as go
from plotly.subplots import make_subplots

from utils import STATS_DIR


def parse_args():
    """
    Parse command line arguments
    
    Returns
    -------
    args : argparse.Namespace
        command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("method", nargs="?", default=None,
                        choices=["bruteforce", "bruteforce2", "backtracking", "compare"],
                        help="Resolution method")
    return parser.parse_args()


def plot_method(data, method):
    """
    Plot execution time and number of combinations for a given method
    
    Parameters
    ----------
    data : dict
        Dictionary containing the execution time and number of combinations for each number of empty cells
    method : str
        Method for which to plot the execution time and number of combinations
    """
    # Extracting data for plotting
    empty_cells = sorted(map(int, data.keys()))
    exec_times = [data[str(empty_count)]['execution_time'] for empty_count in empty_cells]
    n_combinations = [data[str(empty_count)]['n_combinations'] for empty_count in empty_cells]

    # Create a Plotly figure with subplots
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add traces for Execution Time
    fig.add_trace(go.Scatter(x=empty_cells, y=exec_times, mode='lines+markers', name="Execution Time", line=dict(color='blue')), secondary_y=False)

    # Add traces for Number of Combinations
    fig.add_trace(go.Scatter(x=empty_cells, y=n_combinations, mode='lines+markers', name="Number of Combinations", line=dict(color='red')), secondary_y=True)

    # Set the layout
    fig.update_layout(title=f"Execution Time and Number of Combinations for {method.capitalize()}",
                      xaxis_title="Number of Empty Cells",
                      yaxis_title="Execution Time (seconds)",
                      yaxis=dict(title="Number of Combinations", color="red"),
                      legend=dict(x=0.02, y=0.98),
                      margin=dict(l=50, r=50, t=50, b=50),
                      hovermode="x unified")

    # Show the interactive plot
    fig.show()


def compare_methods(data, *methods):
    # Colors for each method
    colors = ["blue", "yellow", "red"]

    # Create figure
    fig = go.Figure()

    max_empty_cells = min(len(data[method]) for method in methods)

    # Plot the curves for each method
    for method in methods:
        values = data[method]
        color = colors[methods.index(method)]

        # Draw the curve
        x = [int(key) for key in values.keys() if int(key) <= max_empty_cells]
        y = [values[key]["execution_time"] for key in values.keys() if int(key) <= max_empty_cells]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=method, line=dict(color=color)))

        # Draw text
        fig.add_annotation(
            x=x[0], y=y[0], text=f"{method} - {y[0]:.2f}", showarrow=False,
            font=dict(size=8, color=color), xshift=10, yshift=10, xanchor="left", yanchor="bottom"
        )

    # Add titles and captions
    fig.update_layout(
        title=f"Comparison of execution time for {' - '.join(methods)}",
        xaxis_title="Number of empty cells",
        yaxis_title="Execution time (seconds)",
        legend=dict(x=0, y=1, traceorder="normal", font=dict(family="sans-serif", size=12))
    )

    # Show interactive graph
    fig.show()


def main():
    method = parse_args().method
    with open(STATS_DIR / f"execution_times.json", "r") as file:
        data = json.load(file)
    if method is not None:
        if method == "compare":
            compare_methods(data, "bruteforce", "bruteforce2", "backtracking")
            compare_methods(data, "bruteforce", "backtracking")
            compare_methods(data, "bruteforce", "bruteforce2")
            compare_methods(data, "bruteforce2", "backtracking")
        else:
            with open(STATS_DIR / f"{method}.json", "r") as file:
                data = json.load(file)
            plot_method(data[method], method)
    else:
        for method in ["bruteforce", "bruteforce2", "backtracking"]:
            plot_method(data[method], method)
        compare_methods(data, "bruteforce", "bruteforce2", "backtracking")
        compare_methods(data, "bruteforce", "backtracking")
        compare_methods(data, "bruteforce", "bruteforce2")
        compare_methods(data, "bruteforce2", "backtracking")


if __name__ == "__main__":
    main()