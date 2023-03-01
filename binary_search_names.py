#only works on sorted list but much faster than linear search

names = [] #sorted list of names you are searching through

search_names = ["Mary Johnson", "Alf Gonzo", "Zach Quinto", "Berry Stone", "Kimberly Jones", "Severous Snape", "Wilbur Williams", "William Kurt", "Harry Styles"]
#names you are looking for in names list

def binary_search(list, target):
    first = 0
    last = len(list) -1 
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

for n in search_names:
    index = binary_search(names, n)
    print(index)