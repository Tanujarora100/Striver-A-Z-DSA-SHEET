from collections import deque


class MyStack:

    def __init__(self):
        self._stack = deque()
        self._size_stack = 0

    def push(self, x: int) -> None:
        self._stack.appendleft(x)
        self._size_stack += 1

    def pop(self) -> int:
        if self._size_stack <= 0:
            return -1
        else:
            popped_ele = self._stack.popleft()
            self._size_stack -= 1
            return popped_ele

    def top(self) -> int:
        return self._stack[0]

    def empty(self) -> bool:
        if self._size_stack <= 0:
            return True
        else:
            return False

    def length(self) -> int:
        return self._size_stack
