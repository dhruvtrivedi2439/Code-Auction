def interpolation_search(arr, x):
    """
    This function performs interpolation search on the given sorted array
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
    while start <= end and x >= arr[start] and x <= arr[end]:
        
        # Calculate the position of the element to be searched using interpolation formula
        pos = start + ((x - arr[start]) * (end - start)) // (arr[end] - arr[start])
        
        # Check if the element is found at the calculated position
        if arr[pos] == x:
            return pos
        
        # If the element is less than the calculated position,
        # discard the right half of the array by updating the end index
        elif arr[pos] > x:
            end = pos - 1
        
        # If the element is greater than the calculated position,
        # discard the left half of the array by updating the start index
        else:
            start = pos + 1
    
    # If the loop completes without finding the value, return -1
    return -1
