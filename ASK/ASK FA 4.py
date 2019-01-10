
def my_sort(lst):
    for i in range(1, len(lst)):

        key = lst[i]

        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def my_sort2(lst):
    for i in range(len(lst)):
        waarde = lst[i]
        for j in range(0, i):
            if waarde<lst[j]:
                waarde, lst[j] = lst[j], waarde
        lst[i] = waarde

list1 = [7, 9, 4, 67, 209, 1]

my_sort(list1)
print(list1)

my_sort2(list1)
print(list1)