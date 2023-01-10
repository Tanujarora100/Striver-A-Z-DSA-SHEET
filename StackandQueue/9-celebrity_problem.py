class solution:
    def celebrity(self, M, n):
        stack = []

        for i in range(n):
            stack.append(i)

        while len(stack) != 1:
            a = stack.pop()
            b = stack.pop()
            if self.knows(a, b, M):
                stack.append(b)
            else:
                stack.append(a)
        candidate = stack[-1]

        # Verify now

        zeroCount = 0
        for i in range(n):
            if M[candidate][i] == 0:
                zeroCount += 1

        if zeroCount != n:
            return -1

        one_count = 0

        for i in range(n):
            if M[i][candidate] == 1:
                one_count += 1

        if one_count != n-1:
            return -1

        return candidate

    def knows(self, a, b, M):
        if M[a][b] == 1:
            return True
        else:
            return False

    def celebrityTwoPointer(self, M, n):
        # code here
        i = 0
        j = n-1
        candidate = -1
        while (i < j):
            if M[j][i] == 1:
                j -= 1
            else:
                i += 1

        candidate = i
        for k in range(n):
            if candidate != k:
                if M[candidate][k] == 1 or M[k][candidate] == 0:
                    return -1

        return candidate
