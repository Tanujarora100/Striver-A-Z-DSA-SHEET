class Solution:
    def fib(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        if n in dp:
            return dp[n]
        dp[n] = self.fib(n-1)+self.fib(n-2)
        return dp[n]

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
