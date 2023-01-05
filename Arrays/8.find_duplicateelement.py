class solution:
    from ast import List

    # Using set to find the duplicate element
    '''
    Time Complexity: O(n)O(n)

    HashSet insertions and lookups have amortized constant time complexities.
    Hence, this algorithm requires linear time,
    since it consists of a single for loop that iterates over each element,
    looking up the element and inserting it into the set at most once.
    Space Complexity: O(n)
    We use a set that may need to store at most n element
    leading to a linear space complexity of O(n).
    '''

    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()
        res = 0
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            else:
                res = nums[i]
        return res

    # Time Complexity-O(NLOGN)
    # Space Complexity-O(N) Tim sort

    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                res = nums[i]
        return res

# Flyod cycle detection
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
