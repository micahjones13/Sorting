# TO-DO: complete the helpe function below to merge 2 sorted arrays
#left = a, right = b


def merge(arrA, arrB):
    # print(arrA, arrB, 'arrays')

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

# starting values for a and b arr index's
    a = 0
    b = 0
    # loop as many times as elements is long to reshape the merged_arr
    for i in range(0, elements):
        # if a is greater than then length of arrA, then it's empty. Fill in merged with arrB automatically
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # same thing here, but b is empty
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # if the value at arrA[a] is less than arrb[b], store that value into merged_arr at that point in loop (i)
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # same thing, but a is greater
        elif arrA[a] > arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1

    # print(merged_arr, 'MERGEDARR')

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION (5 lines)
def merge_sort(arr):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half.
    # eventually each item should be in it's own little list
    # base case
    if len(arr) <= 1:
        return arr
    # find the middle of the array
    mid = len(arr) // 2
    # split the array into 2 - right and left of mid
    split_right = arr[mid:]
    split_left = arr[:mid]
    # print('mid', mid)
    # print(split_right, 'split_right')
    # print(split_left, 'split left')
    # keep splitting the right and left until they are all in they're own little list
    left = merge_sort(split_left)
    right = merge_sort(split_right)
    # put em back together
    arr = merge(left, right)

    return arr


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


my_arr = [9, 6, 4, 7, 8, 1, 0, 2, 5, 3]
arr1 = [6]
arr2 = [9]
# Quicksort from lesson
# pick a pivot, move to right spot


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # select a pivot, often times this is the last or first element
    pivot = arr[-1]
    # move all elements smaller than pivot to left, all greater to right
    left = []
    right = []
    # don't care about last item because that's the pivot
    for i in range(len(arr) - 1):
        item = arr[i]
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return quicksort(left) + [pivot] + quicksort(right)
    # while LHS and RHS are greater than 1, repeat stpes 1-3 on each


# print(quicksort(my_arr))
# print(merge(arr1, arr2))
print(merge_sort(my_arr))


"""


9, 6, 4 , 7, 8, 1, 0, 2, 5, 3

left: 9 6 4 7 8 ||| right: 1 0 2 5 3
again with left
left 9 6 || right 4 7 8
again with left 
left: 9 right 6 



6 9 4 8 7 0 1 2 3 5 
"""
