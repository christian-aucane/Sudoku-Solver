"""
Generate graphs

Plot the execution time of each method
and save the figure in the GRAPHS_DIR folder
"""
import json

import matplotlib.pyplot as plt

from utils import STATS_DIR, GRAPHS_DIR


def plot_method(data, method):
    """
    Plot execution time and number of combinations
    for a given method and save the figure in the GRAPHS_DIR folder

    Args:
        data (dict): Dictionary containing the execution time
            and number of combinations for each number of empty cells
        method (str): Method for which to plot
            the execution time and number of combinations
    """
    _, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("Number of Empty Cells")

    # Runtime curve
    ax1.set_ylabel("Execution Time (seconds)", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.grid(True)

    # Curve for number of combinations
    ax2 = ax1.twinx()
    ax2.set_ylabel("Number of Combinations", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    # Extracting data for plotting
    empty_cells = sorted(map(int, data.keys()))
    exec_times = [
        data[str(empty_count)]["execution_time"]
        for empty_count in empty_cells
    ]
    n_combinations = [
        data[str(empty_count)]["n_combinations"]
        for empty_count in empty_cells
    ]

    # Plot the curves
    ax1.plot(
        empty_cells, exec_times,
        linestyle="-",
        label="Execution Time", color="tab:blue"
    )
    ax2.plot(
        empty_cells, n_combinations,
        linestyle="--",
        label="Number of Combinations", color="tab:red"
    )

    # Add caption
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    plt.title(
        f"Execution Time and Number of Combinations for {method.capitalize()}"
    )
    plt.savefig(GRAPHS_DIR / f"{method}.png")

    plt.close()


def compare_methods(data, *methods):
    """
    Plot the execution time of each method
    and save the figure in the GRAPHS_DIR folder

    Args:
        data (dict): Dictionary containing the execution time for each method
        *methods (str): Methods for which to plot the execution time
    """
    # Colors for each method
    colors = ["b", "y", "r"]

    # Get the maximum number of empty cells
    max_empty_cells = min(len(data[method]) for method in methods)

    # Plot the curves for each method
    for method in methods:
        values = data[method]
        color = colors[methods.index(method)]

        # Draw the curve
        x = [int(key) for key in values.keys() if int(key) <= max_empty_cells]
        y = [
            values[key]["execution_time"]
            for key in values.keys()
            if int(key) <= max_empty_cells
        ]
        plt.plot(x, y, label=method, color=color)

    # Add titles and captions
    plt.title(f"Comparation of execution time for {' - '.join(methods)}")
    plt.xlabel("Number of empty cells")
    plt.ylabel("Execution time (seconds)")
    plt.legend()

    plt.savefig(GRAPHS_DIR / f"{'_'.join(methods)}.png")

    plt.close()


def main():
    """
    Main function
    """
    print("Plotting graphs...")
    with open(STATS_DIR / "execution_times.json", "r") as file:
        data = json.load(file)

    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    for method in data:
        plot_method(data[method], method)

    compare_methods(data, "bruteforce", "bruteforce2", "backtracking")
    compare_methods(data, "bruteforce", "backtracking")
    compare_methods(data, "bruteforce", "bruteforce2")
    compare_methods(data, "bruteforce2", "backtracking")

    print("Graphs saved in", GRAPHS_DIR)


if __name__ == "__main__":
    main()
