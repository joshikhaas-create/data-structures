def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 # joshikhaa laasya
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Main program
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr.sort()  # Ensure array is sorted
print("Sorted array is:", arr)

key = int(input("Enter the element to search: "))
result = binary_search(arr, key)

if result != -1:
    print("Element is found at the index:", result)
else:
    print("Element is not found")
