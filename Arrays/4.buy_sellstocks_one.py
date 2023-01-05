from ast import List


def maxProfit(self, prices: List[int]) -> int:
    minimum = prices[0]
    profit = 0
    for i in range(len(prices)):
        dailyProfit = prices[i]-minimum
        profit = max(profit, dailyProfit)
        minimum = min(minimum, prices[i])
    return profit
