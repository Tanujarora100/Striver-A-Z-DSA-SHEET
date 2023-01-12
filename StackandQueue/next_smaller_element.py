class Solution:
    def help_classmate(self, arr, n):
        stack = []
        answer = []
        stack.append(-1)
        for i in range(n-1, -1, -1):
            while len(stack) > 1 and stack[-1] >= arr[i]:
                stack.pop()
            answer.append(stack[-1])
            stack.append(arr[i])
        return list(reversed(answer))
