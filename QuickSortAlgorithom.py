array = []

for i in range(7):
    array.append(int(input('Enter a number : ')))


# Partition
def partition(a, p, r):
    i = p - 1  # index of smaller element
    x = a[r]  # pivot

    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)


quickSort(array, 0, len(array) - 1)

print('Sorted array list : ')

for i in range(len(array)):
    print(array[i])
