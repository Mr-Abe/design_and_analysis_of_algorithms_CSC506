#!/usr/bin/env python3
"""
sorting_comparator_v2.py

This script compares the performance of various sorting algorithms.
It implements core algorithms (Bubble Sort, Merge Sort, Quick Sort, Insertion Sort, Heap Sort)
with input customization via command-line arguments, and displays the comparative results in both
tabular and bar chart formats. Additionally, it outputs recommendations for further analysis.
"""

import time
import random
import argparse
import copy
import statistics
import matplotlib.pyplot as plt

# -----------------------------
# Sorting Algorithms
# -----------------------------

def bubble_sort(arr):
    number_of_elements = len(arr)
    for i in range(number_of_elements):
        has_swapped = False
        for j in range(0, number_of_elements - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                has_swapped = True
        if not has_swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# -----------------------------
# Utility Functions
# -----------------------------

def generate_random_list(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

def measure_sorting_time(sort_function, arr):
    arr_copy = copy.deepcopy(arr)
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return end_time - start_time

def display_table(results):
    print("\nExecution Times (averages over 20 runs):")
    header = "{:<25} {:>15} {:>15}".format("Algorithm", "Avg (sec)", "Std Dev")
    print(header)
    print("-" * len(header))
    for name, (avg, std) in results.items():
        print("{:<25} {:>15.6f} {:>15.6f}".format(name, avg, std))

# -----------------------------
# Main Execution and Testing
# -----------------------------

def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithm Comparator")
    parser.add_argument("--size", type=int, default=1000, help="Number of elements in the list")
    parser.add_argument("--min_val", type=int, default=1, help="Minimum value for list elements")
    parser.add_argument("--max_val", type=int, default=10000, help="Maximum value for list elements")
    args = parser.parse_args()

    data = generate_random_list(args.size, args.min_val, args.max_val)

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Insertion Sort": insertion_sort,
        "Heap Sort": heap_sort
    }

    execution_results = {}
    num_runs = 20

    for name, func in sorting_algorithms.items():
        times = []
        for _ in range(num_runs):
            elapsed = measure_sorting_time(func, data)
            times.append(elapsed)
        avg_time = statistics.mean(times)
        std_time = statistics.stdev(times)
        execution_results[name] = (avg_time, std_time)
        print(f"{name} took an average of {avg_time:.6f} seconds (Std Dev: {std_time:.6f}).")

    display_table(execution_results)

    # Visualization using matplotlib
    algorithms = list(execution_results.keys())
    avg_times = [execution_results[alg][0] for alg in algorithms]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, avg_times, color='skyblue')
    plt.xlabel("Sorting Algorithms")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title("Average Execution Time Comparison (20 Runs)")
    plt.tight_layout()
    plt.show()

    # Analysis and Optimization Recommendations (Output for further analysis)
    print("\nAnalysis and Optimization Recommendations:")
    print("1. Provide detailed dataset sizes, execution times, and memory usage metrics for further analysis.")
    print("2. Compare algorithms: Bubble Sort exhibits O(n^2) performance; others are generally O(n log n) in average cases.")
    print("3. Optimizations implemented: Early termination in Bubble Sort and efficient heapify in Heap Sort.")
    print("4. Future improvements: In-place Quick Sort and hybrid methods for small subarrays.")

if __name__ == "__main__":
    main()