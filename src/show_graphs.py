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
                        choices=["bruteforce", "bruteforce2", "backtracking"],
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

def main():
    method = parse_args().method
    if method is not None:
        with open(STATS_DIR / f"{method}.json", "r") as file:
            data = json.load(file)
        plot_method(data, method)
    else:
        for method in ["bruteforce", "bruteforce2", "backtracking"]:
            with open(STATS_DIR / f"{method}.json", "r") as file:
                data = json.load(file)
            plot_method(data, method)


if __name__ == "__main__":
    main()