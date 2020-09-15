A = []

for i in range(6):
    A.append(int(input('Enter a number : ')))
    print(A)
    
def insertSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while(i >= 0 and A[i] > key) :
            A[i+1] = A[i]
            i = i - 1

        A[i+1] = key

insertSort(A)

print("Sorted Array")

for k in range(len(A)):
        print(A[k])

