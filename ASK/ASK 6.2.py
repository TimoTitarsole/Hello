def binary_search(lst, target):
    links = 0
    rechts = len(lst) - 1
    while links <= rechts:
        midden = round((links + rechts) / 2)
        if lst[midden] < target:
            links = midden + 1
        if lst[midden] > target:
            rechts = midden -1
        if lst[midden] == target:
            return True
    return False

list1 = ['f', 'b', 'c', 'd', 'e']
list1.sort()
invoer = 'e'
print(binary_search(list1, invoer))