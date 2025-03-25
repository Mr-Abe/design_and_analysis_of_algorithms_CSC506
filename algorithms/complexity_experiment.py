'''
Write two Python functions for the same task (e.g. sum of the first n integers) 
– one using a simple loop and one using a doubly nested loop 
– and time them on increasing n. 
This isn’t a strict lab exercise, but by printing timestamps or using Python’s time module, you can observe how the runtime grows. 
It will reinforce the concept of linear vs quadratic time in a tangible way. (For instance, summing with one loop is O(n); 
summing with two nested loops is O(n²) – you’ll notice the nested version slows down much faster as n grows.)
'''


import time



def linear_sum(n):
    total = 0

    for value in range (1, n):
        total = value + total

    return total


def nested_sum(n):
    total = 0

    for value in n:
        for value_2 in range (1, value):
            total = value + value_2

    return total


def main():
    n = int(input("How many iterations would you like to run? "))
    start_time = time.time()
    linear_sum(n)
    end_time = time.time()
    print("Linear sum took: ", end_time - start_time)


if __name__ == "__main__":
    main()