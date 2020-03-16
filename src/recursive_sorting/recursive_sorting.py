# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    iofA = 0
    iofB = 0
    # TO-DO
    for i in range(elements):
        # if an index lies beyond the bounds of the array,
        # we've reached the end, so add element from the other array
        if len(arrA) <= iofA:
            # add element to the merged array and shift index
            merged_arr[i] = arrB[iofB]
            iofB += 1
        elif len(arrB) <= iofB:
            merged_arr[i] = arrA[iofA]
            iofA += 1
        # compare the two smallest unmerged values
        elif arrB[iofB] < arrA[iofA]:
            # if the right is smaller add it to the merged_arr
            merged_arr[i] = arrB[iofB]
            iofB += 1
        else:
            # if the left is smaller add it to the merged_arr
            merged_arr[i] = arrA[iofA]
            iofA += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    # 1. While your data set contains more than one item, split it in half
    else:
        middle = len(arr)//2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        # 2. Once you have gotten down to a single element, you have also *sorted* that element
        # 3. Start merging your single lists of one element together into larger, sorted sets
        # 4. Repeat step 3 until the entire data set has been reassembled
        return merge(merge_sort(left_arr), merge_sort(right_arr))


my_arr = [1, 5, 8, 4, 2, 9, 6, 0, 7, 3]
print(merge_sort(my_arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
