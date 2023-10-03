"""
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing).
Then doing some arithmetic to calculate the position of each object in the output 
sequence.

Time Complexity: O(n+k) where n is the number of elements in input array and k is the
range of input.
"""


def counting_sort(nums: list) -> list:
    """
    Counting Sort
    Time complexity: O(n+k)
    """
    count_arr = [0] * (max(nums) + 1)
    output_nums = [0] * len(nums)

    for i in nums:
        count_arr[i] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in nums:
        output_nums[count_arr[i] - 1] = i

    return output_nums
