"""
Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 
1945.

Time complexity: O(nlogn)
"""


def merge(left: list, right: list) -> list:
    """
    This function merges two sorted arrays into one sorted array.

    Time complexity: O(n)
    """
    i, j = 0, 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr


def merge_sort(arr: list) -> list:
    """
    This function returns the sorted array using merge sort algorithm.

    Time complexity: O(nlogn)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
