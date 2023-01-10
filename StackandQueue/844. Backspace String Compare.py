class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            stack = []
            for i in S:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s) == build(t)
