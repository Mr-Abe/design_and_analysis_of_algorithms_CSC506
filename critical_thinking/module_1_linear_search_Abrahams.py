import time

def linearSearch(arr, target):
    i = 0

    # check while i < instead of <= to avoid bounds error
    while i < len(arr):
        if arr[i] == target:
            print(f'target value {target} found at position {i + 1}')
            # ends the loop when target found
            return
        
        i += 1

    print(f"Target {target} not found in list.")
        

def testRun(target):
    '''
    multiple lists filled to over 1000 slots to aid with analyzing run time.
    '''
    
    # 1) First run: target value '7' is at the end       
    arr_end = (([31, 3, 54, 50, 203, 59, 201] * 21) * 1000) + [42, 99, 7]
    print(f"First Run:\n  Target: {target}\n  List has {len(arr_end)} elements")
    start_time = time.time()
    linearSearch(arr_end, target)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    # 2) Second run: target value '7' is at the front
    arr_front = [7] + (([31, 3, 54, 50, 203, 59, 201] * 21) * 1000) + [42, 99]
    print(f"Second Run:\n  Target: {target}\n  List has {len(arr_front)} elements")
    start_time = time.time()
    linearSearch(arr_front, target)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    # 3) Third run: list does not contain the target
    arr_missing = (([31, 3, 54, 50, 203, 59, 201, 42, 99] * 21) * 1000) + [123, 456, 789, 111, 222, 333]
    print(f"Third Run:\n  Target: {target}\n  List has {len(arr_missing)} elements")
    start_time = time.time()
    linearSearch(arr_missing, target)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    # 4) Fourth run: list contains the target multiple times
    arr_multiple = ([12, 5, 63, 87, 4, 88, 9, 3, 22, 3] * 1000) + ([7, 31, 3, 7, 54, 50, 7, 203, 59, 201] * 15)
    print(f"Fourth Run:\n  Target: {target}\n  List has {len(arr_multiple)} elements")
    start_time = time.time()
    linearSearch(arr_multiple, target)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")


if __name__=='__main__':
    # value to be found
    target = 7

    testRun(target)

