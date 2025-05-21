"""
This script benchmarks the performance of Merge Sort and Quicksort implementations
on datasets of different sizes and input characteristics (sorted, reverse sorted, and random).
It tracks both execution time (in milliseconds) and memory usage (in kilobytes).

Dependencies:
- MergeSort.py (must contain a merge_sort function)
- QuickSort.py (must contain a quick_sort function)
"""

import time
import tracemalloc
import random
import csv
from MergeSort import merge_sort
from QuickSort import quick_sort

def benchmark(algorithm, input_data, repeat=3):
    """
    Benchmarks the provided sorting algorithm.

    Args:
        algorithm (function): The sorting function to benchmark.
        input_data (list): The input list to be sorted.
        repeat (int): Number of times to repeat the benchmark for averaging.

    Returns:
        tuple: (average execution time in ms, average memory usage in KB)
    """
    total_time = 0
    total_memory = 0

    for _ in range(repeat):
        data_copy = input_data[:]
        tracemalloc.start()
        start_time = time.perf_counter()
        algorithm(data_copy)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += (end_time - start_time) * 1000  # Convert to ms
        total_memory += peak / 1024  # Convert to KB

    avg_time = round(total_time / repeat, 2)
    avg_memory = round(total_memory / repeat, 2)
    return avg_time, avg_memory

def generate_input(size, input_type):
    """
    Generates a list of integers based on the specified input type.

    Args:
        size (int): The number of elements in the list.
        input_type (str): One of 'sorted', 'reverse', or 'random'.

    Returns:
        list: Generated list of integers.
    """
    if input_type == 'sorted':
        return list(range(size))
    elif input_type == 'reverse':
        return list(range(size, 0, -1))
    elif input_type == 'random':
        return random.sample(range(size * 2), size)
    else:
        raise ValueError("Invalid input_type. Choose from 'sorted', 'reverse', 'random'.")

def run_benchmarks():
    """
    Runs the benchmarks on Merge Sort and Quicksort for various input types and sizes.
    Saves the results to CSV files.
    """
    sizes = [100, 200, 500, 1000]
    input_types = ['sorted', 'reverse', 'random']
    results_merge = []
    results_quick = []

    for size in sizes:
        for input_type in input_types:
            data = generate_input(size, input_type)

            merge_time, merge_mem = benchmark(merge_sort, data)
            quick_time, quick_mem = benchmark(quick_sort, data)

            results_merge.append([size, input_type, merge_time, merge_mem])
            results_quick.append([size, input_type, quick_time, quick_mem])

    # Write Merge Sort results
    with open('merge_sort_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Size', 'InputType', 'Time(ms)', 'Memory(KB)'])
        writer.writerows(results_merge)

    # Write Quicksort results
    with open('quick_sort_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Size', 'InputType', 'Time(ms)', 'Memory(KB)'])
        writer.writerows(results_quick)

if __name__ == '__main__':
    run_benchmarks()
