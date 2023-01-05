import sys


class Solution:
    def findSum(self, A, N):
        maxi = -sys.maxsize
        mini = sys.maxsize
        for i in range(len(A)):
            maxi = max(maxi, A[i])
            mini = min(mini, A[i])
        return maxi+mini
