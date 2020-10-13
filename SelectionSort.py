def selection_sort(a):
    n = len(a)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if a[i] < a[smallest]:
                smallest = i
        a[j], a[smallest] = a[smallest], a[j]
    print(a)


a = []
for i in range(6):
    a.append(input())

selection_sort(a)
