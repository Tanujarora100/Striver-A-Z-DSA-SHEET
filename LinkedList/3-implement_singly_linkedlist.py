class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def deleteAtHead(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteAtTail(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


LL = LinkedList()
LL.append(5)
LL.append(6)
LL.append(7)
LL.prepend(9)
LL.print_list()
LL.deleteAtHead()
print()
print()
LL.print_list()
