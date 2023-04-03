def binary_search(arr, x):
    """
    This function performs binary search on the given sorted array
    to find the index of the given element.

    Parameters:
    arr (list): The sorted array or list to be searched.
    x: The value to be searched in the array.

    Returns:
    int: The index of the element if found, -1 otherwise.
    """
    
    # Set the initial values for the start and end indices
    start = 0
    end = len(arr) - 1
    
    # Loop until the start index is less than or equal to the end index
    while start <= end:
        
        # Calculate the middle index
        mid = (start + end) // 2
        
        # Check if the middle element is the desired value
        if arr[mid] == x:
            
            # If found, return the index of the element
            return mid
        
        # If the middle element is less than the desired value,
        # discard the left half of the array by updating the start index
        elif arr[mid] < x:
            start = mid + 1
        
        # If the middle element is greater than the desired value,
        # discard the right half of the array by updating the end index
        else:
            end = mid - 1
    
    # If the loop completes without finding the value, return -1
    return -1
