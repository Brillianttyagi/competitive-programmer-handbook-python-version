"""
Maximum subarray sum
O(n3) solution
"""


def maximum_subarray_sum(arr: list) -> list:
    """
    This function returns the maximum subarray sum of the given array.

    Time complexity: O(n3)
    """
    max_ans = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            ans = 0
            for k in range(i, j + 1):
                ans += arr[k]
            max_ans = max(max_ans, ans)

    return max_ans
