
class solution:
    def rev(self, q):
        if len(q) == 0:
            return
        element = q.pop(0)
        self.rev(q)
        q.append(element)

    def reverse(self, q):
        stack = []
        queue = []
        while q:
            stack.append(q.pop(0))
        while stack:
            queue.append(stack.pop())
        return queue


q = [1, 2, 3, 4, 5]
ob = solution()
print(ob.reverse(q))
