"""
Maximum subarray sum
O(n2) solution
"""


def maximum_subarray_sum(arr: list) -> list:
    """
    This function returns the maximum subarray sum of the given array.

    Time complexity: O(n2)
    """
    max_ans = 0
    for i in range(len(arr)):
        ans = 0
        for j in range(i, len(arr)):
            ans += arr[j]
            max_ans = max(max_ans, ans)
    return max_ans
