
from typing import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    count = 0
    slow = head
    while slow:
        count = count+1
        slow = slow.next
    middle = count//2
    temp = head
    for _ in range(middle-1):
        temp = temp.next
    temp.next = temp.next.next
    return head


def deleteMiddleUsingPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return None
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = prev.next.next
    return head
