def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key: # joshikhaa laasya
            return i   # joshikhaa laasya
    return -1          


# Example usage
arr = [10, 25, 30, 45, 50, 75]
key = int(input("Enter the element to search: "))

result = linear_search(arr, key)

if result != -1:
    print(f"Element {key} found at position {result}.")
else:
    print(f"Element {key} not found in the list.")
