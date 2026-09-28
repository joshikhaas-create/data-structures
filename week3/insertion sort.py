# Insertion Sort Implementation in Python

def insertion_sort(arr):
    for i in range(1, len(arr)):  # joshikhaa laasya
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Main program
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Original array:", arr)

insertion_sort(arr)

print("Sorted array:", arr)
