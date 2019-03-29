class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedListClass:
    """
    Class with solutions to different linked list related problems
    """

    @staticmethod
    def add_node(head: Node, val):
        """

        :param head:
        :param node:
        :return:
        """
        while head.next is not None:
            head = head.next
        node = Node(val)
        head.next = node

    @staticmethod
    def print_linkedlist(linkedlist: Node):
        """

        :param linkedlist:
        :return:
        """
        string = ""
        string += str(linkedlist.val)
        linkedlist = linkedlist.next
        while linkedlist is not None:
            string += ("-> {}".format(linkedlist.val))
            linkedlist = linkedlist.next
        print(string)

    @staticmethod
    def remove_duplicates(head: Node):
        """
        Remove nodes with duplicate values

        Time Complexity: O(n)
        Space Complexity: O(n) (Worst case)

        :param head: given linked list
        :return:
        """
        if not head or not head.val:
            return
        value_set = set()
        first = None

        while head is not None:
            if head.val not in value_set:
                value_set.add(head.val)
                first = head
            else:
                first.next = head.next
            head = head.next
        return first

    @staticmethod
    def remove_duplicates_no_buffer(head: Node):
        """
        Remove nodes with duplicate values, without using a buffer

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        :param head: given linked list
        :return:
        """
        if not head or not head.val:
            return

        current = head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.val != current.val:
                    runner = runner.next
                else:
                    runner.next = runner.next.next
            current = current.next
        return current


if __name__ == '__main__':
    print("Testing linked lists")
    n1 = Node(5)
    LinkedListClass.add_node(n1, 5)
    LinkedListClass.add_node(n1, 6)
    LinkedListClass.add_node(n1, 7)
    LinkedListClass.add_node(n1, 8)
    LinkedListClass.add_node(n1, 9)

    LinkedListClass.print_linkedlist(n1)

    print("Removing redundancies")
    LinkedListClass.remove_duplicates(n1)
    LinkedListClass.print_linkedlist(n1)

    n2 = Node(5)
    LinkedListClass.add_node(n2, 5)
    LinkedListClass.add_node(n2, 6)
    LinkedListClass.add_node(n2, 7)
    LinkedListClass.add_node(n2, 8)
    LinkedListClass.add_node(n2, 9)
    print("Removing redundancies without using buffer")
    LinkedListClass.remove_duplicates_no_buffer(n2)
    LinkedListClass.print_linkedlist(n2)
