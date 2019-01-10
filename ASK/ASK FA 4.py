
def my_sort1(lst):
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


def linear_search(list, key, idx=0):
    if list:
        if list[0] == key:
            return 'De index van' + ' ' + str(key) + ' ' + 'is' + ' ' + str(idx) + '.'

        s = linear_search(list[1:], key, (idx + 1))
        if s is not False:
            return s

    return 'Het getal' + ' ' + str(key) + ' ' + 'staat niet in de lijst!'


def binary_search(list, key, start=0, end=None):
    if end is None:
        end = len(list) - 1

    if start > end:
        return 'Het getal' + ' ' + str(key) + ' ' + 'staat niet in de lijst!'

    mid = (start + end) // 2

    if key == list[mid]:
        return 'De index van' + ' ' + str(key) + ' ' + 'is' + ' ' + str(mid) + '.'

    if key < list[mid]:
        return binary_search(list, key, start, mid - 1)

    return binary_search(list, key, mid + 1, end)


list1 = [100, 7, 5, 21, 16, 2, 1]
search = int(input('Welk getal zoek je?'))

my_sort1(list1)
print(list1)

my_sort2(list1)
print(list1)

print(lineair_search(list1, search, idx=0))

print(binary_search(list1, search, start=0, end=None))