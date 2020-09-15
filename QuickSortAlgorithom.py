array = []

for i in range(7):
    array.append(int(input('Enter a number : ')))
    print(array)

def partition(array, p, r):
    i = p - 1 #index of smaller element
    x = array[r] #pivot

    for j in range(p, r):
        if array[j] <= x :
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i+1]
    return (i + 1)

def quickSort(array, p, r):
    if p < r :
        q = partition(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)

quickSort(array, 0, len(array)-1)

print('Sorted array list : ')

for i in range(len(array)):
    print(array[i])
