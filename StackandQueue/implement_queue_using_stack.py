class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
# Time complexity : O(1). Аppending an element to a stack is an O(1) operation.
# Space complexity : O(n). We need additional memory to store the queue elements

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output

    # Time Complexity-O(1)
    # Space Complexity-O(1)


'''
        Time complexity: Amortized O(1), Worst-case O(n).
        In the worst case scenario when stack s2 is empty, the algorithm pops n elements from stack s1 and pushes nn elements to s2,
        where nn is the queue size. This gives 2n operations, which is O(n).
        But when stack s2 is not empty the algorithm has
        O(1) time complexity. So what does it mean by Amortized O(1)O(1)
        Space complexity : O(1)O(1).
'''
