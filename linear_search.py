def linear_search(arr, x):
    """
    This function performs linear search on the given array
    to find the index of the given element.

    Parameters:
    arr (list): The array or list to be searched.
    x: The value to be searched in the array.

    Returns:
    int: The index of the element if found, -1 otherwise.
    """
    
    # Loop through every element in the array
    for i in range(len(arr)):
        
        # Check if the current element matches the desired value
        if arr[i] == x:
            
            # If found, return the index of the element
            return i
    
    # If the loop completes without finding the value, return -1
    return -1
