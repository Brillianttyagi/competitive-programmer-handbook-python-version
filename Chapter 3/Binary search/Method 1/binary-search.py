"""
Binary Search Algorithm
-----------------------
* Binary search is a fast search algorithm with run-time complexity of Ο(log n).
* This search algorithm works on the principle of divide and conquer.
* For this algorithm to work properly, the data collection should be in the sorted form.
* Binary search looks for a particular item by comparing the middle most item of the 
  collection.
* If a match occurs, then the index of item is returned.
* If the middle item is greater than the item, then the item is searched in the 
  sub-array to the left of the middle item.
* Otherwise, the item is searched for in the sub-array to the right of the middle item.
* This process continues on the sub-array as well until the size of the subarray reduces
  to zero.

Time Complexity
---------------
Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)
"""


def binary_search(data, item):
    """
    Binary Search Algorithm
    -----------------------
    :param data: collection of items (sorted list)
    :param item: item to be searched
    :return: index of item if found, otherwise -1
    """
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data[mid] == item:
            return mid
        elif item < mid[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
