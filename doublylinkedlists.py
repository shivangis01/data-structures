"""
Data Structures - Doubly Linked List

Pros over SLL:
  - Allows easy traversal in both directions
  - Allows easy deletion of given node, or easy insertion before a given node

Cons vs SLL:
  - Required more memory for each node for storing the previous pointer
"""


class Node:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, val):
        if self.head.val == val:
            self.head = self.head.next
        head = self.head
        while head.next is not None:
            if head.val == val:
                prevnode = head.prev
                nextnode = head.next
                prevnode.next = nextnode
                break
            else:
                head = head.next

    def display_list(self):
        head = self.head
        while head.next is not None:
            print("{} ->".format(head.val))
            head = head.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    print("Print DLL")

    dll.display_list()

    print("Print DLL after deleting a node")
    dll.delete_node(2)
    dll.display_list()
