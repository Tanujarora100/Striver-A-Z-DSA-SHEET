
# Starting Point ofLinkedListCycle

from typing import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node_seen = set()
    while head is not None:
        if head in node_seen:
            return head
        node_seen.add(head)
        head = head.next
    return None
# Space Complexity-O(N)
# Time Complexity-O(N)


def hasCycleOptimized(self, head):
    if head is None:
        return None
    slow = head
    fast = head
    entry = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            while slow != entry:
                entry = entry.next
                slow = slow.next
            return slow
    return None
# Space Complexity-O(1)
# Time Complexity-O(N)
