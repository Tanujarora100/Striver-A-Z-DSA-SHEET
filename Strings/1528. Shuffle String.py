from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restore = []
        for i in range(len(indices)):
            restore.append(s[indices.index(i)])
        return "".join(restore)
