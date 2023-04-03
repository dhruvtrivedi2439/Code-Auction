def exponential_search(arr, x):
    """
    This function performs exponential search on the given sorted array
    to find the index of the given element.

    Parameters:
    arr (list): The sorted array or list to be searched.
    x: The value to be searched in the array.

    Returns:
    int: The index of the element if found, -1 otherwise.
    """
    
    # If the first element of the array matches the element to be searched
    # then return the index 0
    if arr[0] == x:
        return 0
    
    # Set an initial value for the index variable
    i = 1
    
    # Double the index i until it is less than the length of the array
    while i < len(arr) and arr[i] <= x:
        i *= 2
    
    # Perform binary search on the elements between the last index
    # and the current index value i to find the position of the element
    return binary_search(arr, x, i // 2, min(i, len(arr)))
    
def binary_search(arr, x, start, end):
    """
    This function performs binary search on the given sorted array
    between the given start and end indices.

    Parameters:
    arr (list): The sorted array or list to be searched.
    x: The value to be searched in the array.
    start (int): The starting index of the array to be searched.
    end (int): The ending index of the array to be searched.

    Returns:
    int: The index of the element if found, -1 otherwise.
    """
    
    # Loop until the start index is less than or equal to the end index
    while start <= end:
        
        # Calculate the middle index
        mid = start + (end - start) // 2
        
        # If the middle element matches the value to be searched, return its index
        if arr[mid] == x:
            return mid
        
        # If the middle element is greater than the value to be searched,
        # discard the right half of the array by updating the end index
        elif arr[mid] > x:
            end = mid - 1
        
        # If the middle element is less than the value to be searched,
        # discard the left half of the array by updating the start index
        else:
            start = mid + 1
    
    # If the value is not found, return -1
    return -1
