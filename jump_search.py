import math

def jump_search(arr, x):
    """
    This function performs jump search on the given sorted array
    to find the index of the given element.

    Parameters:
    arr (list): The sorted array or list to be searched.
    x: The value to be searched in the array.

    Returns:
    int: The index of the element if found, -1 otherwise.
    """

    # Find the length of the array
    n = len(arr)
    
    # Calculate the jump size by taking the square root of the length of the array
    jump_size = int(math.sqrt(n))

    # Set the initial values of the variables for the start index and end index
    start = 0
    end = jump_size
    
    # Jump through the array until the value of the element at the end index is greater than the value to be searched
    while end < n and arr[end] <= x:
        start = end
        end += jump_size
    
    # Perform linear search on the elements between the start and end indices to find the position of the element
    for i in range(start, min(end+1, n)):
        if arr[i] == x:
            return i
    
    # If the value is not found, return -1
    return -1
