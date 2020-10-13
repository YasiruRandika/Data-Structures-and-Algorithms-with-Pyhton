# Insert Sort Algorithm
def insertSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key


A = []

for i in range(10):
    A.append(int(input('Enter a number : ')))

insertSort(A)

print("\nSorted Array")

print(A)
