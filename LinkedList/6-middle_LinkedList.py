from typing import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

# Brute Force Approach
    def bruteForce(self, head):
        if head is None:
            return None
        n = 0
        temp = head
        while temp != None:
            n = n+1
            temp = temp.next

        temp = head
        for i in range(n/2):
            temp = temp.next
        return temp
