from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] not in intersect:
                intersect[nums1[i]] = 1
            else:
                intersect[nums1[i]] += 1
        print(intersect)
        for i in range(len(nums2)):
            if nums2[i] in intersect and intersect.get(nums2[i]) > 0:
                res.append(nums2[i])
                intersect[nums2[i]] -= 1
        print(intersect)
        return res


'''
The time complexity of the code provided is O(n). The first for loop has a time complexity of O(n) as it iterates over nums1,
and the second for loop also has a time complexity of O(n) as it iterates over nums2.
The if statement in the second for loop has a constant time complexity, O(1),
as it only involves a hash table lookup. 
The append() method which is called once for each iteration of the second for loop, has a constant time complexity of O(1).

The space complexity of the code is also O(n). 
The intersect dictionary will require O(n) space to store the counts of each element in nums1,
and the res list will also require O(n) space to store the intersecting elements from nums2.


'''


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    c1 = collections.Counter(nums1)
    # Counter is  O(N)
    c2 = collections.Counter(nums2)
    # Counter is  O(N)
    c3 = c1 & c2
    # Intersection of Commmon Elements
    return list(c3.elements())


'''
    The time complexity of the code  provided is O(n). The Counter() function has a time complexity of O(n), 
    and it is called twice in the code, once for nums1 and once for nums2. 
    The & operator, which is used to calculate the intersection of the two counters,
    also has a time complexity of O(n). 
    Finally, the elements() method of the Counter object has a time complexity of O(n), as 
    it must iterate over the elements of the counter to create a list.

The space complexity of the code is also O(n). The Counter() function requires O(n) 
space to store the counts of each element in the input list, 
and the resulting Counter object will also require O(n) space. 
The c3 variable, which is used to store the intersection of the two counters, will also require O(n) space.
Finally, the list() function will require O(n) space to store the list of elements returned by elements().
'''


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    i = 0
    j = 0
    nums1.sort()
    nums2.sort()
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return res


'''
The time complexity of the code  provided is O(n * log(n)). 
The sort() method has a time complexity of O(n * log(n)) for both nums1 and nums2, 
and the while loop has a time complexity of O(n) 
as it iterates over the elements of nums1 and nums2. 
The if statement and the two elif statements each have a constant time complexity, O(1).
The append() method, which is called once for each iteration of the while loop, has a constant time complexity of O(1).

The space complexity of the code is O(n).
The res list will require O(n) space to store the intersecting elements from nums1 and nums2.
'''
