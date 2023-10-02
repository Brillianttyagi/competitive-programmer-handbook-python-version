"""
Maximum subarray sum
O(n2) solution
"""

def maximum_subarray_sum(arr: list) -> list:
    """
    This function returns the maximum subarray sum of the given array.
    
    Time complexity: O(n2)
    """
    max_ans = -999999999
    ans = 0 
    for i in arr:
        ans+=i
        max_ans = max(max_ans, ans)
        if ans<0:
            ans=0
    return max_ans
