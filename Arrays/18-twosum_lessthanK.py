from typing import List


class solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < k:
                    answer = max(answer, sum)
        return answer
    # Time Complexity-O(N)
    # Space Complexity-O(1)


# Approach-Using Binary Search


    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        if nums[0] > k:
            return -1
        max_sum = -1
        for i in range(0, len(nums)):
            curr_num = nums[i]
            if curr_num > k:
                continue
            lo, hi = i+1, len(nums)

            while lo < hi:
                mid = lo+(hi-lo)//2
                if curr_num + nums[mid] >= k:
                    hi = mid
                else:
                    lo = mid+1
            if lo-1 > i:
                curr_sum = curr_num + nums[lo-1]
                max_sum = max(curr_sum, max_sum)


# Time Complexity-O(NLOGN) for Sorting
# Space Complexity-O(N) for tim sort


    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        start = 0
        end = len(nums)-1
        while start < end:
            prefix_sum = nums[start]+nums[end]
            # it can be lower than k
            if prefix_sum < k:
                answer = max(answer, prefix_sum)
                start = start+1
            # second case it can be greater than K
            else:
                end = end-1
        return answer

    # Approach 3-Using Count Sort
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = 1000
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
        return answer


'''
Time Complexity: O(n+m), where mm corresponds to the range of values in the input array.
Space Complexity: O(m) to count each value.
'''
