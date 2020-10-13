def insertion_sort(a):
    for j in range(1, len(a)):
        i = 0

        # For Descending Order
        while a[j] < a[i]:
            i += 1
        key = a[j]

        for k in range(j-i):
            a[j-k] = a[j-k-1]

        a[i] = key


A = []

for i in range(10):
    A.append(int(input('Enter a number : ')))

insertion_sort(A)

print("\nSorted Array")

print(A)