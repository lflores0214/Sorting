# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            # check if the array at j is less than the current smallest index
            # if it is j becomes the smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # print(arr)

    return arr


my_arr = [1, 5, 8, 4, 2, 9, 6, 0, 7, 3]
# print(selection_sort(my_arr))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through array
    print(arr)
    for i in range(len(arr)-1):
        # check if the element at current index is greater than the element to the right
        if arr[i] > arr[i+1]:
            # if it is than swap the two elements
            arr[i], arr[i+1] = arr[i+1], arr[i]
            # run loop again until they are all sorted
            bubble_sort(arr)

    return arr


bubble_sort(my_arr)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
