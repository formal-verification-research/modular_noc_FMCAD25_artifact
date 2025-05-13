from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import re

results_dir = Path("results/")
plot_dir = Path("plot")
plot_dir.mkdir(exist_ok=True)

def get_threshold(filename: str) -> int:
    """Extracts the threshold value from the filename."""
    match = re.search(r"threshold_(\d+)_", filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Didn't find threshold in filename: {filename}")

def plot_noise(directory: Path):
    """Plots inductive and resistive noise from CSV files in a directory."""
    noc_size = directory.name
    csv_files = list(directory.glob("*.csv"))

    # Plot inductive noise
    fig, ax = plt.subplots(figsize=(3.3, 2.7))
    lines = []
    labels = []
    thresholds = []

    for file in csv_files:
        if "inductive" in file.name.lower():
            threshold = get_threshold(file.name)
            thresholds.append(threshold)
            label = f">= {threshold}"
            labels.append(label)
            try:
                data = pd.read_csv(file)
                line, = ax.plot(data["Clock Cycle"], data["Probability"], linewidth=1.0)
                lines.append(line)
            except KeyError:
                print(f"Warning: 'ClockCycle' or 'Probability' column not found in {file.name}")
            except Exception as e:
                print(f"Error reading {file.name}: {e}")

    sorted_indices = sorted(range(len(thresholds)), key=lambda k: thresholds[k])
    ax.set_prop_cycle(None)  # Reset color cycle
    for i in sorted_indices:
        if lines:
            ax.plot(lines[i].get_xdata(), lines[i].get_ydata(), linewidth=1.0)
    sorted_labels = [labels[i] for i in sorted_indices]

    ax.grid(True)
    ax.legend(sorted_labels, loc="lower right")
    ax.set_xlabel("Clock cycles")
    ax.set_ylabel("Probability")
    ax.autoscale(axis='x', tight=True)
    ax.autoscale(axis='y', tight=True)
    png_filename = f"{noc_size}_inductive_py.png"
    fig.savefig(plot_dir / png_filename, dpi=600, bbox_inches='tight')
    plt.close(fig)

    # Plot resistive noise
    fig, ax = plt.subplots(figsize=(3.3, 2.7))
    lines = []
    labels = []
    thresholds = []

    for file in csv_files:
        if "resistive" in file.name.lower():
            threshold = get_threshold(file.name)
            thresholds.append(threshold)
            label = f">= {threshold}"
            labels.append(label)
            try:
                data = pd.read_csv(file)
                line, = ax.plot(data["Clock Cycle"], data["Probability"], linewidth=1.0)
                lines.append(line)
            except KeyError:
                print(f"Warning: 'ClockCycle' or 'Probability' column not found in {file.name}")
            except Exception as e:
                print(f"Error reading {file.name}: {e}")

    sorted_indices = sorted(range(len(thresholds)), key=lambda k: thresholds[k])
    ax.set_prop_cycle(None)  # Reset color cycle
    for i in sorted_indices:
        if lines:
            ax.plot(lines[i].get_xdata(), lines[i].get_ydata(), linewidth=1.0)
    sorted_labels = [labels[i] for i in sorted_indices]

    ax.grid(True)
    ax.legend(sorted_labels, loc="lower right")
    ax.set_xlabel("Clock cycles")
    ax.set_ylabel("Probability")
    ax.autoscale(axis='x', tight=True)
    ax.autoscale(axis='y', tight=True)
    png_filename = f"{noc_size}_resistive_py.png"
    fig.savefig(plot_dir / png_filename, dpi=600, bbox_inches='tight')
    plt.close(fig)

# Iterate through subdirectories in the results directory
for item in results_dir.iterdir():
    if item.is_dir() and item.name not in (".", ".."):
        plot_noise(item)