from ast import List
import math


def maxSubArraySum(self, arr, N):
    maxi = arr[0]
    res = 0
    for i in range(N):
        res = res+arr[i]
        maxi = max(maxi, res)
        if res < 0:
            res = 0
            # Carrying a Minus Sum will decrease our maximum SubArraySum so we do not take it
    return maxi
# Time Complexity-O(N)
# Space Complexity-O(1)


def maxSubArray(self, nums: List[int]) -> int:
    max_sub = -math.inf
    for i in range(len(nums)):
        curr = 0
        for j in range(i, len(nums)):
            curr += nums[j]
            max_sub = max(curr, max_sub)
    return max_sub
