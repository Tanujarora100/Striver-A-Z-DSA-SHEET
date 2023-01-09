def climbStairs(self, n):
    memo = {}
    memo[1] = 1
    memo[2] = 2

    def climb(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
    return climb(n)


def climbStairs(self, n: int, memo={}) -> int:  # including memo to store result
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
    return memo[n]
