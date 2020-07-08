def binary_search(sorted_list, length, value):
    start = 0
    end = length - 1
    while start <= end:
        mid = int((start + end) / 2)
        if value == sorted_list[mid]:
            print("\nEntered number %d is present at : %d" % (value, mid))
            return -1
        elif value < sorted_list[mid]:
            end = mid - 1
        elif value > sorted_list[mid]:
            start = mid + 1
    print("\nvalue is not present")
    return -1


list = []

size = int(input("Enter size of list: \t"))

for n in range(size):
    num = int(input("Enter the number: \t"))
    list.append(num)

list.sort()
print('\n the sorted list is:', list)

x = int(input("\nEnter the number to search: "))

binary_search(list, size, x)