class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_at_head(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.newNode.next = self.head
            self.head.prev = newNode
            self.newNode = self.head
        self.length += 1

    def add_at_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_at_head(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return data

    def get_length(self):
        return self.length

    def delete_at_tail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1
        return data


linked_list = DoublyLinkedList()
linked_list.add_at_tail(1)
linked_list.add_at_tail(2)
linked_list.add_at_tail(3)
print(linked_list.get_length())  # 3
print(linked_list.delete_at_head())  # 1
print(linked_list.get_length())  # 2
