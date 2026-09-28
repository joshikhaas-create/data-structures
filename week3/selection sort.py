# Selection Sort Implementation in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):# joshikhaa laasya
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main program
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Original array:", arr)

selection_sort(arr)

print("Sorted array:", arr)
