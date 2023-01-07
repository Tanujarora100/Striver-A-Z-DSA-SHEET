from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        start = 0
        sum_list = []
        end = n-1
        while start < end:
            if nums[start]+nums[end] == target:
                sum_list.append(nums[start])
                sum_list.append(nums[end])
                break
            elif nums[start]+nums[end] < target:
                start = start+1
            else:
                end = end-1
        return sum_list
# Two Pointer ask the Interviewer if we can sort the array first.

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in sum_dict:
                return [i, sum_dict[complement]]
            sum_dict[nums[i]] = i
