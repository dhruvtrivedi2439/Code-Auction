def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose a pivot element and partition the array around it
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)
