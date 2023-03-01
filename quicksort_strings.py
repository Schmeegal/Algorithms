import sys

names = ["Mary Johnson", "Alf Gonzo", "Zach Quinto", "Berry Stone", "Kimberly Jones", "Severous Snape", "Wilbur Williams", "William Kurt", "Harry Styles"]

def quicksort(list):
    if len(list) <= 1:
        return list
    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]
    for n in list[1:]:
        if n <= pivot:
            less_than_pivot.append(n)
        else:
            greater_than_pivot.append(n)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_n = quicksort(names)
#print(sorted_n)
for n in sorted_n:
    print(n)

#in terminal: python3 quicksort_string.py > filename.txt
#this will output sorted name to a text document