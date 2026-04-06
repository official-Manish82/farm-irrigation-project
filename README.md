# Quick Sort Performance Analysis

## Overview
This project implements Quick Sort algorithm with comprehensive time complexity analysis by measuring execution time for different input sizes (n).

## Files Included

### 1. **Exp1.cpp** - Main C++ Program
Implements Quick Sort with two modes:
- **Mode 1**: Manual Quick Sort (user provides input array)
- **Mode 2**: Performance Analysis (generates random arrays and measures time)

#### Key Features:
- **Quick Sort Implementation**: Standard Lomuto partition scheme
- **Partition Function**: Efficiently divides array around pivot
- **Random Array Generation**: Creates arrays with random elements (0-9999)
- **High-Resolution Timer**: Uses `chrono::high_resolution_clock` for accurate microsecond measurements
- **Dynamic Memory**: Allocates arrays on the heap for large sizes
- **Data Logging**: Saves results to `quicksort_analysis.txt`

#### Test Sizes (n):
100, 500, 1000, 2000, 5000, 10000, 15000, 20000

### 2. **plot_quicksort.py** - Python Plotting Script
Reads the analysis data and generates:
- Line graph showing Time vs n
- Visual representation saved as PNG
- Formatted table output

#### Requirements:
- Python 3.x
- matplotlib
- numpy

## How to Use

### Step 1: Compile the C++ Program
```bash
g++ -o Exp1 Exp1.cpp -std=c++11
```

### Step 2: Run Performance Analysis
```bash
./Exp1
# Select option 2
```

This generates:
- Console output with timing data
- `quicksort_analysis.txt` file with n and time values

### Step 3: Generate Graph
```bash
python plot_quicksort.py
```

This creates:
- `quicksort_analysis.png` - performance graph
- Console output of the analysis table

## Output Files Generated

1. **quicksort_analysis.txt** - Tab-separated values
   ```
   n	Time(microseconds)
   100	7
   500	38
   1000	94
   ... (more data)
   ```

2. **quicksort_analysis.png** - Performance visualization graph

## Algorithm Analysis

### Time Complexity:
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n²)

### Space Complexity: O(log n) - recursive call stack

## Performance Results (Sample)
```
n          Time (µs)
100        7
500        38
1000       94
2000       211
5000       567
10000      1048
15000      1551
20000      2501
```

The graph shows a near-linear relationship between n and execution time, indicating efficient O(n log n) average case performance.

## Features

✓ Efficient Quick Sort implementation
✓ Accurate microsecond-level timing
✓ Scalable to large arrays (up to 20000+ elements)
✓ Random array generation
✓ Automatic data logging
✓ Python visualization
✓ Interactive menu

## Notes

- Timing is measured in **microseconds** for precision
- Each test creates a fresh random array
- Results may vary slightly between runs due to:
  - System load
  - Cache effects
  - Random data variation
- For more accurate results, run multiple times and average
