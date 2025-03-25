#!/usr/bin/env python3
"""
sorting_comparator_v1.py

This script compares the performance of various sorting algorithms.
It implements core algorithms (Bubble Sort, Merge Sort, Quick Sort) and includes placeholders
for extended algorithms (Insertion Sort, Heap Sort) to be implemented by the final submission. The script allows input customization
via command-line arguments and visualizes the execution times using a bar chart.
"""

import time            # For performance measurement
import random          # For generating random lists
import argparse        # For command-line argument parsing
import copy            # To make deep copies of lists
import matplotlib.pyplot as plt  # For visualization


def bubble_sort(unsorted_list):
    """
    Sorts a list using the Bubble Sort algorithm.
    
    Parameters:
        unsorted_list (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    number_of_elements = len(unsorted_list)  # Get the number of elements in the list
    # Loop over each element in the list
    for current_index in range(number_of_elements):
        has_swapped = False  # Flag to detect any swap in the inner loop
        # Traverse the list from the beginning to the unsorted portion
        for compare_index in range(0, number_of_elements - current_index - 1):
            # Compare adjacent elements and swap if necessary
            if unsorted_list[compare_index] > unsorted_list[compare_index + 1]:
                unsorted_list[compare_index], unsorted_list[compare_index + 1] = unsorted_list[compare_index + 1], unsorted_list[compare_index]
                has_swapped = True  # Mark that a swap occurred
        # If no elements were swapped, the list is already sorted
        if not has_swapped:
            break
    return unsorted_list

def merge_sort(unsorted_list):
    """
    Sorts a list using the Merge Sort algorithm.
    
    Parameters:
        unsorted_list (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    if len(unsorted_list) > 1:
        middle_index = len(unsorted_list) // 2  # Find the midpoint of the list
        left_half = unsorted_list[:middle_index]  # Split the list into left half
        right_half = unsorted_list[middle_index:]  # and right half

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = sorted_index = 0
        
        # Merge the sorted halves into the original list
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                unsorted_list[sorted_index] = left_half[left_index]
                left_index += 1
            else:
                unsorted_list[sorted_index] = right_half[right_index]
                right_index += 1
            sorted_index += 1

        # Copy any remaining elements of left_half
        while left_index < len(left_half):
            unsorted_list[sorted_index] = left_half[left_index]
            left_index += 1
            sorted_index += 1

        # Copy any remaining elements of right_half
        while right_index < len(right_half):
            unsorted_list[sorted_index] = right_half[right_index]
            right_index += 1
            sorted_index += 1

    return unsorted_list

def quick_sort(unsorted_list):
    """
    Sorts a list using the Quick Sort algorithm.
    
    Parameters:
        unsorted_list (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    # Base case: if the list is empty or has one element, it is already sorted
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        # Choose a pivot element (middle element)
        pivot_value = unsorted_list[len(unsorted_list) // 2]
        # Partition the list into three parts: less than, equal to, and greater than the pivot
        less_than_pivot = [element for element in unsorted_list if element < pivot_value]
        equal_to_pivot = [element for element in unsorted_list if element == pivot_value]
        greater_than_pivot = [element for element in unsorted_list if element > pivot_value]
        # Recursively sort the less_than and greater_than partitions and combine them with the pivot
        return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# Algorithms to be implemented later

def insertion_sort(unsorted_list):
    """
    Placeholder for Insertion Sort.
    Builds a sorted list by sequentially inserting elements into their correct position.
    
    Parameters:
        unsorted_list (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    # TODO: Implement Insertion Sort algorithm.
    # For now, simply return the input list without modifications.
    # return unsorted_list
    pass

def heap_sort(unsorted_list):
    """
    Placeholder for Heap Sort.
    Sorts the list by constructing a max heap and repeatedly extracting the maximum element.
    
    Parameters:
        unsorted_list (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    # TODO: Implement Heap Sort algorithm.
    # For now, simply return the input list without modifications.
    # return unsorted_list
    pass

# Helper functions

def generate_random_list(list_size, minimum_value, maximum_value):
    """
    Generates a list of random integers.
    
    Parameters:
        list_size (int): The number of elements in the list.
        minimum_value (int): The minimum possible integer value.
        maximum_value (int): The maximum possible integer value.
        
    Returns:
        list: A list containing randomly generated integers.
    """
    return [random.randint(minimum_value, maximum_value) for _ in range(list_size)]

def measure_sorting_time(sort_function, input_list):
    """
    Measures the time taken by a sorting function to sort a list.
    
    Parameters:
        sort_function (function): The sorting function to be tested.
        input_list (list): The list to be sorted.
        
    Returns:
        float: The elapsed time in seconds.
    """
    # Create a deep copy of the input list to ensure identical inputs for each sort function
    list_copy = copy.deepcopy(input_list)
    # Record the start time
    start_time = time.perf_counter()
    # Execute the sorting algorithm
    sort_function(list_copy)
    # Record the end time
    end_time = time.perf_counter()
    # Return the total time taken to sort the list
    return end_time - start_time


def main():
    # Parse command-line arguments for customizing input parameters
    parser = argparse.ArgumentParser(description="Sorting Algorithm Comparator")
    parser.add_argument("--size", type=int, default=1000, help="Number of elements in the list")
    parser.add_argument("--min_val", type=int, default=1, help="Minimum value for list elements")
    parser.add_argument("--max_val", type=int, default=10000, help="Maximum value for list elements")
    arguments = parser.parse_args()

    # Generate a random dataset based on the provided parameters
    unsorted_data = generate_random_list(arguments.size, arguments.min_val, arguments.max_val)

    # Dictionary mapping descriptive algorithm names to their corresponding functions
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        # Placeholders for extended algorithms:
        "Insertion Sort": insertion_sort,
        "Heap Sort": heap_sort
    }

    # Dictionary to store execution times for each sorting algorithm
    algorithm_execution_times = {}

    # Iterate through each sorting algorithm, measure its performance, and store the results
    for algorithm_name, sorting_function in sorting_algorithms.items():
        elapsed_time = measure_sorting_time(sorting_function, unsorted_data)
        algorithm_execution_times[algorithm_name] = elapsed_time
        # Print the execution time for the current algorithm
        print(f"{algorithm_name} took {elapsed_time:.6f} seconds.")

    # -----------------------------
    # Visualization: Create a bar chart using matplotlib
    # -----------------------------
    plt.figure(figsize=(10, 6))  # Set the figure size
    # Create a bar chart with algorithm names on the x-axis and execution times on the y-axis
    plt.bar(algorithm_execution_times.keys(), algorithm_execution_times.values(), color='skyblue')
    plt.xlabel("Sorting Algorithms")  # Label the x-axis
    plt.ylabel("Execution Time (seconds)")  # Label the y-axis
    plt.title("Execution Time Comparison of Sorting Algorithms")  # Set the chart title
    plt.tight_layout()  # Adjust layout to prevent label clipping
    plt.show()  # Display the bar chart

# Execute main() if this script is run directly
if __name__ == "__main__":
    main()