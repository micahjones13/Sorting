# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # takes first index, therefore splitting it into sorted vs unsorted
        cur_index = i
        # sets smallest_index equal to cur_index, which means the first index [0] is smallest rn
        # same as not even using cur_index. could just set smallest_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop again through arr, comparing the cur_index (i) to new index var j
        # if at any point in the loop arr[smallest_index] > arr[j], then it's no longer the smallest
        for j in range(cur_index, len(arr)):
            # print(i, 'i', j, 'j', arr[j], 'arrj', arr[i], 'arri')
            if arr[smallest_index] > arr[j]:
                # replace smallest with new smalles
                smallest_index = j
                # print(j, 'J after IF')

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # print(arr, 'after swap')

    return arr


"""

Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )




"""
# TO-DO:  implement the Bubble Sort function below
# Bubble sort compares neaighbors and rearannges based on the comparison


def bubble_sort(arr):
    # loop through the array
    for i in range(len(arr)):
        # print(i, 'i')
        # loop again so you can compare to neighbor
        # need len(arr)- 1 or else out of bounds error
        for j in range(0, len(arr)-1):
            # if j is bigger than it's neighbor j+1,
            if arr[j] > arr[j+1]:
                # swap the postions
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr, 'iterative')
    # print(arr)
    return arr


# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
#! Made this just to test what it looked like with only 1 for loop. It rearranges the first number, but stops after that
# def bubble_test(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#     print(arr)
#     return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


my_arr = [9, 6, 4, 7, 8, 1, 0, 2, 5, 3]

# selection_sort(my_arr)
# bubble_sort(my_arr)
# bubble_test(my_arr)


"""
tried this for bubble sort first, but it's basically the select sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        cur_index = i
        for j in range(i, len(arr)):
            if arr[cur_index] > arr[j]:
                arr[cur_index], arr[j] = arr[j], arr[cur_index]
                i += 1
            else:
                i += 1
    print(arr)
    return arr


"""
