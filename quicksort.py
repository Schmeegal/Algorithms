import sys

numbers = [5,2,7,15,7,86,43,74]

def quicksort(list):
    '''
    Another recursive sort function (T O(nlogn) but worst case O(n^2))
    Faster than recursion.py but still slow for large arrays
    More often used than recursive merge sort
    uncomment print statement to help understand how function works
    must have break point(if statement)
    '''
    if len(list) <= 1:
        return list
    #create a pivot from first element
    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]
    for num in list[1:]:
        if num <= pivot:
            less_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)
    #print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)    

sorted_numbers = quicksort(numbers)
print(sorted_numbers)