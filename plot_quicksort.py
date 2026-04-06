import matplotlib.pyplot as plt
import numpy as np

# Read data from the analysis file
data = []
with open('quicksort_analysis.txt', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines[1:]):  # Skip header
        parts = line.strip().split('\t')
        if len(parts) == 2:
            n = int(parts[0])
            time = int(parts[1])
            data.append((n, time))

# Extract n and time values
n_values = [d[0] for d in data]
time_values = [d[1] for d in data]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, 'bo-', linewidth=2, markersize=8, label='Quick Sort')

# Add labels and title
plt.xlabel('Number of Elements (n)', fontsize=12)
plt.ylabel('Time (microseconds)', fontsize=12)
plt.title('Quick Sort Performance Analysis', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

# Format the plot
plt.tight_layout()

# Save the figure
plt.savefig('quicksort_analysis.png', dpi=300)
print("Graph saved as 'quicksort_analysis.png'")

# Display the plot
plt.show()

# Print analysis
print("\n=== Quick Sort Analysis ===")
print(f"{'n':<10} {'Time (µs)':<15}")
print("-" * 25)
for n, t in data:
    print(f"{n:<10} {t:<15}")
