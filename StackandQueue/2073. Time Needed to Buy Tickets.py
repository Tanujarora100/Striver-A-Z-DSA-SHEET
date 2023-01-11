from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        i = 0
        while tickets[k] > 0:
            if tickets[(i % len(tickets))] > 0:
                tickets[(i % len(tickets))] -= 1
                time_taken += 1
                i = i % len(tickets)+1
            else:
                i = i % len(tickets)+1
        return time_taken
