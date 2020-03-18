# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    # iterate (loop) over the array
    for i in range(len(arr)):
        # if the element matches the tartget value
        if arr[i] == target:
          # return that element
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low <= high:
      mid = (low + high)//2
      # if the target matches the middle you found it
      if arr[mid] == target:
        return mid
      # else if the target is smaller than the middle 
      elif arr[mid] > target:
        # assign a new high end of the array
        high = mid-1
      #else if the target is bigger than the middle 
      else:
        # Do it again with new highs and lows
        low = mid+1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    # if the target matches the middle you found it
    if arr[middle] == target:
      return middle
    # else if the target is smaller than the middle 
    elif arr[middle] > target:
      # assign a new high end of the array
      high = middle -1
      return binary_search_recursive(arr, target, low, high)
    #else if the target is bigger than the middle 
    else:
      # assign a new low end of the array
      low = middle + 1
      # Do it again with new highs and lows
      return binary_search_recursive(arr, target, low, high)
