from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
        # Time Complexity-O(N^2)
        # Space Complexity-O(N)
        # Without Sorting approach
    # 2nd Approach using a tuple and Set at the end

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # s = set()
        nums.sort()
        leaders = []
        n = len(nums)
        for i in range(n):
            # Trick to skip the duplicates in the array
            if i > 0 and nums[i - 1] == nums[i]:
                continue  # Skip duplicates
            start = i+1
            end = n-1
            while start < end:
                if nums[i]+nums[start]+nums[end] == 0:
                    leaders.append((nums[start], nums[i], nums[end]))
                    start = start+1
                    end = end-1
                elif nums[start]+nums[end]+nums[i] > 0:
                    end = end-1
                else:
                    start = start+1
        return set(leaders)

    '''
    This code has a time complexity of O(n^2) and a space complexity of O(n),
    since it iterates over the array nums twice and stores all of the triplets in leaders
    '''

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            else:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    # 4th Approach variation of 2nd approach without using set at the end

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
