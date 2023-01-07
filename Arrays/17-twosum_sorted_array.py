from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):  # O(n)
            new_target = target-numbers[idx]
            lft, rght = idx+1, len(numbers)-1
            while lft <= rght:  # O(logn)
                mid = lft+(rght-lft)//2
                if numbers[mid] == new_target:
                    return [idx+1, mid+1]
                elif numbers[mid] > new_target:
                    rght = mid-1
                else:
                    lft = mid+1
    # Time Complexity-O(LOGN)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            if numbers[start]+numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start]+numbers[end] < target:
                start = start+1
            else:
                end = end-1
    # Time Complexity-O(N)
