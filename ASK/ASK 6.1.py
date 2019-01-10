def linear_search(lst, target):
    for char in lst:
        sans = False
        if char == target:
            sans = True
    return sans

def linear_search_index(lst, target):
    count = 0
    for char in lst:
        if char == target:
            return count
        count += 1


list1 = ['a', 'b', 'c', 'd', 'e']
invoer = 'e'
#print(linear_search(list1, invoer))
print(linear_search_index(list1, invoer))