import sys

numbers = [34,2,67,58,34,10,3,44]

def merge_sort(list):
    '''
    Recursive merge sort - T O(nlogn)
    uncomment print statement to help understand function
    '''
    if len(list) <= 1:
        return list
    middle_index = len(list)//2
    left_values = merge_sort(list[:middle_index])
    right_values = merge_sort(list[middle_index:])
    #print("%15s %-15s" % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index +=1
        else:
            sorted_values.append(right_values[right_index])
            right_index +=1
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values


sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
