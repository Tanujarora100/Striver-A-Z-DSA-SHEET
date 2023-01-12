class TwoStack:
    # Time Complexity
    # O(1) for push operation, as it only takes constant time to push an element into the stack.
    # O(1) for pop operation, as it only takes constant time to pop out an element out of the stack.
    # Space Complexity O(N), where N is the size of the array used for two stack's implementation.
    def __init__(self, s):
        self.size = s
        self.arr = [0] * self.size
        self.top1 = -1
        self.top2 = self.size

    # Push function for the first stack
    def push1(self, val):
        # If overflow exists, return
        if self.top1 + 1 == self.top2:
            return
        self.top1 += 1
        # Ek aage badha do and vaha par insert kardo
        self.arr[self.top1] = val

    # Push function for the second stack
    def push2(self, val):
        # If overflow exists, return
        if self.top2 - 1 == self.top1:
            return
        self.top2 -= 1
        # Right to left aa rahe hai to ek peeche leh jao index and insert kardo
        self.arr[self.top2] = val

    # Pop function for the first stack
    def pop1(self):
        # If underflow exists, return -1
        if self.top1 == -1:
            return -1
        # self.top1 -= 1
        # stack1 is not empty, then we decrement top1 by 1 and return the value of Arr[top1+1].
        return self.arr[self.top1 + 1]

    # Pop function for the second stack
    def pop2(self):
        # If underflow exists, return -1
        if self.top2 == self.size:
            return -1

        self.top2 += 1
        return self.arr[self.top2 - 1]
