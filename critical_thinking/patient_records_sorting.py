"""
Patient Records Sorting System
Enhancing the efficiency of the hospital's patient records system by comparing Bubble Sort and Merge Sort.
"""

import time
import copy
import random
import datetime

def random_date(start, end):
    """Generate random dates."""
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + datetime.timedelta(days=random_days)

def generate_patient_records(num_records):
    """List of dummy patient records."""
    records = []
    # List of names for random selection
    names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia"]
    
    # Define the range for random date generation
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    
    # Generate a unique set of IDs 
    unique_ids = list(range(1, num_records + 1))
    random.shuffle(unique_ids)
    
    for i in range(num_records):
        record = {
            "id": unique_ids[i],
            "name": random.choice(names),
            "dob": random_date(start_date, end_date).strftime("%Y-%m-%d")
        }
        records.append(record)
    return records

def bubble_sort(records, key="id"):
    """Sorts the patient records using Bubble Sort based on the specified key."""
    n = len(records)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break
    return records

def merge_sort(records, key="id"):
    """Sorts the patient records using Merge Sort based on the specified key."""
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left_half = merge_sort(records[:mid], key)
    right_half = merge_sort(records[mid:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def measure_sorting_time(sort_func, records, key="id"):
    records_copy = copy.deepcopy(records)
    start = time.perf_counter()
    sort_func(records_copy, key)
    end = time.perf_counter()
    return end - start

def get_positive_int(prompt):
    """Prompt the user for a positive integer and validate the input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Main testing block
if __name__ == "__main__":
    num_records = get_positive_int("How many patients would you like to test? ")
    num_runs = get_positive_int("How many times would you like to run the sorting tests? ")

    bubble_times = []
    merge_times = []

    for run in range(1, num_runs + 1):
        print(f"\nRun {run}:")
        # Generate a fresh set of patient records for each run
        records = generate_patient_records(num_records)

        # Measure sorting times for Bubble Sort and Merge Sort
        bt = measure_sorting_time(bubble_sort, records)
        mt = measure_sorting_time(merge_sort, records)

        bubble_times.append(bt)
        merge_times.append(mt)

        print(f"  Bubble Sort Time: {bt:.6f} seconds")
        print(f"  Merge Sort Time: {mt:.6f} seconds")

    # Calculate and display average execution times
    avg_bubble_time = sum(bubble_times) / num_runs
    avg_merge_time = sum(merge_times) / num_runs

    print("\nAverage Execution Times:")
    print(f"  Average Bubble Sort Time: {avg_bubble_time:.6f} seconds")
    print(f"  Average Merge Sort Time: {avg_merge_time:.6f} seconds")