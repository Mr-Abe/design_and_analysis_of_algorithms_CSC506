'''
Write two Python functions for the same task (e.g. sum of the first n integers) 
- one using a simple loop and one using a doubly nested loop 
- and time them on increasing n. 
This isn't a strict lab exercise, but by printing timestamps or using Python's time module, you can observe how the runtime grows. 
It will reinforce the concept of linear vs quadratic time in a tangible way. (For instance, summing with one loop is O(n); 
summing with two nested loops is O(n²) 
- you’ll notice the nested version slows down much faster as n grows.)
'''


import time



def linear_sum(n):
    total = 0

    for value in range (1, n + 1): # range is exclusive, so we add 1 to n we could have used sum(range(1, n + 1))
        total += value

    return total


def nested_sum(n):
    total = 0

    for value in range (1, n + 1):
        for value_2 in range (1, value):
            total += value_2

    return total


def algorithm_time(func, n):
    start_time = time.perf_counter()
    func(n)
    end_time = time.perf_counter()
    
    return end_time - start_time


def print_tabulated_data(title, data):
    print(f"\n{title}:")
    for key, value in data.items():
        print(f"  n = {key:<8} => {value:.8f} seconds")

def main():
    # Number of test cases
    n = int(input("How many different values of n would you like to test? "))

    # Input values for n
    values = [int(input(f"Enter value #{i + 1}: ")) for i in range(n)]

    linear_sum_times = {}
    nested_sum_times = {}

    # Collect timing data
    for value in values:
        linear_sum_times[value] = algorithm_time(linear_sum, value)
        nested_sum_times[value] = algorithm_time(nested_sum, value)

    # Print the timing comparison
    print_tabulated_data("Linear Sum (O(n)) Times", linear_sum_times)
    print_tabulated_data("Nested Sum (O(n²)) Times", nested_sum_times)


if __name__ == "__main__":
    main()