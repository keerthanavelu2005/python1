def heapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[i] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

print("Enter the array size: \n")
n = int(input())
a = []
print("Enter ", n, "Elements : ")
for i in range(n):
       value = int(input())
       a.append(value)
heapSort(a)
print("after sorting the values : ")
for k in a:
       print(k)


