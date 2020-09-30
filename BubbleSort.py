def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    print(a)

a = []
for i in range(6):
    a.append(input())

bubble_sort(a)
