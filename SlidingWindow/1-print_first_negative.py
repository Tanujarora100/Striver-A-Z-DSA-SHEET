class Solution:
    def printFirstNegativeInteger(A, N, K):
        i = 0
        j = 0
        res = []
        ans = []
        while j < N:
            if A[j] < 0:
                res.append(A[j])
            if j-i+1 < K:
                j += 1
            else:
                ans.append(res[0]) if len(res) > 0 else ans.append(0)
                if A[i] < 0:
                    res.pop(0)
                i += 1
                j += 1
        return ans
