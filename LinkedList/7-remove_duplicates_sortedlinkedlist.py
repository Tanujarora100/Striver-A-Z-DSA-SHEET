# REMOVE DUPLICATES FROM SORTED LINKEDLIST

from typing import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def removeDuplicates(head):
    if head is None:
        return None
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next     # skip duplicated node
        cur = cur.next     # not duplicate of current node, move to next node
    return head

# No need to use a Map as it is already sorted
