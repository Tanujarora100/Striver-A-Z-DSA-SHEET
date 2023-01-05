from typing import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def hasCycle(self, head: Optional[ListNode]) -> bool:
    node_seen = set()
    while head != None:
        if head in node_seen:
            return True
        node_seen.add(head)
        head = head.next
    return False
# Space Complexity-O(N)
# Time Complexity-O(N)


def hasCycleOptimized(self, head) -> bool:
    if head is None:
        return None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
# Space Complexity-O(1)
# Time Complexity-O(N)


def hasCycleThird(self, head) -> bool:
    if head is None:
        return None
    curr = self.head
    while curr != None:
        if curr.data == -1:
            return True
        curr.data = -1
        curr = curr.next
    return False
# Space Complexity-O(1)
# Time Complexity-O(N)
