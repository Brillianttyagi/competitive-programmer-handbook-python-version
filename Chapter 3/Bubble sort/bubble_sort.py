"""
Bubble sort algorithm
Time complexity: O(n^2)
"""
def bubble_sort(arr:list) -> list:
    """
    Bubble sort algorithm
    
    Time complexity: O(n^2)
    """
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr

