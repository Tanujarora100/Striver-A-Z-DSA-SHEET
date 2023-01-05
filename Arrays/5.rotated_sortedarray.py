from ast import List


def check(self, nums: List[int]) -> bool:
    count = 0
    # Edge Case missed-->[1,1,1]
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            count = count+1
    if nums[len(nums)-1] > nums[0]:
        count = count+1
    return count <= 1


'''
[1,2,3,4,5]
[3,4,5,1,2]
        3<4-0
        4<5-0
        5>1-1
        1<2-1
        2>3-1
'''
# If it is rotated then one element must be greater so count should be less than 1
# If it is not rotated and only sorted then count must be equal to zero

# check if array is sorted


def arraySortedOrNot(self, arr, n):
    count = 0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            count = count+1
    return count < 1
# Count should always be less than 1

    '''
    3,4,5,1,2,3,4,5,1,2
    1,2,3,4,5 present hai isme
    sorted agar present hai in unsorted+unsorted--> return true
    '''


def check(self, nums: List[int]) -> bool:
    res = '_'.join(str(c) for c in sorted(nums))+'_'
    res2 = '_'.join(str(c) for c in nums) + '_'
    return res in res2 + res2
