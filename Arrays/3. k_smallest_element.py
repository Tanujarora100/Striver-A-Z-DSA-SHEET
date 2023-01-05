import heapq


def kthSmallest(self, arr, l, r, k):
    arr.sort()
    return arr[k-1]
# Time Complexity-O(NLOGN)
# Space Complexity-O(N) in worst case in tim sort


def kthSmallest(self, arr, l, r, k):
    s = set(arr)
    for i in s:
        if k == 1:
            return arr[i]
        k -= 1


def findKthLargest(self, nums, k):
    pq = []
    for i in nums:
        heapq.heappush(pq, i)
        if len(pq) == k+1:
            heapq.heappop(pq)
    return heapq.heappop(pq)
# Time Complexity-O(NLOGK)
# Space Complexity-O(K)
