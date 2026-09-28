# Bubble Sort Implementation in Python

def bubble_sort(arr): # joshikhaa laasya
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Main program
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
