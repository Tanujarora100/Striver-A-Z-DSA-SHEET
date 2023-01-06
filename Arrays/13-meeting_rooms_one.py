import heapq
from typing import List


class solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


# Next meeting ka starting time check karlo ending time to hai hi apne pass simple intuition
'''
The time complexity of this code is O(N log N), since it involves sorting the intervals
which has a time complexity of O(N log N), and looping through the intervals, which has a time complexity of O(N).
The space complexity is O(1), since it does not involve storing any additional data structures.
'''

'''
The time complexity of this code is O(N log N), since it involves creating the heap and looping through the intervals
both of which have a time complexity of O(N log N).
The space complexity is O(N), since it involves storing all the intervals in the heap.
'''


def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    heapq.heapify(intervals)
    max_end_time = 0
    while intervals:
        start, end = heapq.heappop(intervals)
        if start < max_end_time:
            return False
        else:
            max_end_time = max(max_end_time, end)
    return True
