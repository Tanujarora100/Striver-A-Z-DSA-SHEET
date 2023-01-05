from ast import List


def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)
    length = len(nums)
    result = [0] * length
    for i in range(0, length):
        result[(i+k) % length] = nums[i]
    nums[:] = result
# Time Complexity-O(N)
# Space Complexity-O(N)


def reverse(self, nums: list, start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start = start+1
        end -= 1


def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    self.reverse(nums, 0, n-1)
    self.reverse(nums, 0, k-1)
    self.reverse(nums, k, n-1)

# Time Complexity-O(N)
# Space Complexity-O(1)


A = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(A, k))
