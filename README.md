# MSCS-532 Assignment 2: Divide-and-Conquer Sorting Algorithms

This repository contains implementations of two classic divide-and-conquer sorting algorithms in Python, along with a benchmarking framework to evaluate their performance on different types of input data.

## Contents

- `MergeSort.py`: Implementation of Merge Sort (stable, O(n log n), uses extra space)
- `QuickSort.py`: Implementation of Quick Sort (in-place, average O(n log n), worst-case O(n²))
- `benchmark.py`: Benchmarking script that evaluates both algorithms on datasets of varying size and structure
- `merge_sort_results.csv`: Output file containing Merge Sort benchmark results
- `quick_sort_results.csv`: Output file containing Quick Sort benchmark results

## Algorithms

### Merge Sort
- Time Complexity: O(n log n) for all cases
- Space Complexity: O(n) due to auxiliary arrays
- Stable: Yes

### Quick Sort
- Average Time Complexity: O(n log n)
- Worst-case Time Complexity: O(n²) on sorted or reverse-sorted data
- Space Complexity: O(log n) on average (for recursion stack)
- Stable: No

## Benchmarking

The `benchmark.py` script evaluates both sorting algorithms using:
- Input sizes: 100, 200, 500, 1000 elements
- Input types: sorted, reverse-sorted, and random
- Metrics recorded: execution time (ms) and peak memory usage (KB)

Each test is repeated 3 times, and average values are saved to `.csv` files for easy analysis.

## How to Run

1. Make sure all files are in the same directory.
2. Run the benchmarking script:
   ```bash
   python benchmark.py
   ```
3. This will generate two CSV files:
   - `merge_sort_results.csv`
   - `quick_sort_results.csv`

These contain the average execution time and memory usage for each input configuration.

## Requirements

- Python 3.x
- No third-party packages required (uses standard `time`, `random`, `csv`, and `tracemalloc` modules)

## Notes

- The Merge Sort implementation returns a new sorted list.
- The Quick Sort implementation sorts the list in-place.
- The benchmark script uses defensive copying to ensure consistent input across algorithms.