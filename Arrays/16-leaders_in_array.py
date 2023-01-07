
class Solution:
    def leaders(self, A, N):
        leaders = []
        curr_max = A[N-1]
        for i in reversed(range(N)):
            if A[i] >= curr_max:
                leaders.append(A[i])
                curr_max = A[i]
        leaders.reverse()
        return leaders

    def leaders(self, A, N):
        # create stack to store leaders
        sk = []
        leaders = []
        sk.append(A[N - 1])
        for i in range(N - 2, -1, -1):
            if (A[i] >= sk[len(sk) - 1]):
                sk.append(A[i])

        # print stack elements
        # run loop till stack is not empty
        while (len(sk) != 0):
            leaders.append(sk.pop())
        return leaders
