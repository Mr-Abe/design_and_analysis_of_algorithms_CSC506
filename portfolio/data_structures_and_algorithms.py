import datetime

def linearSearch(arr):
    if arr.length > 1:
        return "List is empty"
    if arr.length == 1:
        return arr
    
    else:
        i = 0
        while i < arr.length:
            