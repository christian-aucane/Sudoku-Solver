import json

import matplotlib.pyplot as plt

from utils import STATS_DIR

GRAPHS_DIR = STATS_DIR / "graphs"

def plot_method(data, method):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.set_xlabel("Number of Empty Cells")

    # Runtime curve
    ax1.set_ylabel("Execution Time (seconds)", color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.grid(True)
    
    # Curve for number of combinations
    ax2 = ax1.twinx()
    ax2.set_ylabel("Number of Combinations", color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Extracting data for plotting
    empty_cells = sorted(map(int, data.keys()))
    exec_times = [data[str(empty_count)]['execution_time'] for empty_count in empty_cells]
    n_combinations = [data[str(empty_count)]['n_combinations'] for empty_count in empty_cells]

    # Plot the curves
    ax1.plot(empty_cells, exec_times, marker='o', linestyle='-', label="Execution Time", color='tab:blue')
    ax2.plot(empty_cells, n_combinations, marker='s', linestyle='--', label="Number of Combinations", color='tab:red')

    # Add caption
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    plt.title(f"Execution Time and Number of Combinations for {method.capitalize()}")
    plt.savefig(GRAPHS_DIR / f"{method}.png")  # Save the graph to a specified file

    plt.close()

def main():
    print("Plotting graphs...")
    with open(STATS_DIR / "execution_times.json", "r") as file:
        data = json.load(file)
    
    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    for method, data in data.items():
        plot_method(data, method)

    print("Done!")


if __name__ == "__main__":
    main()