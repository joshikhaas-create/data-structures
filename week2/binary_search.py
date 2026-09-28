def binary_search(arr, key, low, high):
    if low > high:   # Base case: not found
        return -1
    
    mid = (low + high) // 2 # joshikhaa laasya
    
    if arr[mid] == key:
        return mid   # Found at index mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)  # Search left half
    else:
        return binary_search(arr, key, mid + 1, high) # Search right half


# Example usage
arr = sorted([10, 25, 30, 45, -50, 75])  # Sorted array
print("Sorted array:", arr)

key = int(input("Enter the element to search: "))
result = binary_search(arr, key, 0, len(arr) - 1)

if result != -1:
    print(f"Element {key} found at position {result}.")
else:
    print(f"Element {key} not found in the array.")
