from optional import Optional


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    curr = head
    prev = None
    while curr != None:
        next_Node = curr.next
        curr.next = prev
        prev = curr
        curr = next_Node
    return prev
# Recursive Function.


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
