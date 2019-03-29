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

        :param head: given linked list
        :return:
        """
        if not head or not head.val:
            return
        value_set = set()
        first = Node(None)

        while head is not None:
            if head.val not in value_set:
                value_set.add(head.val)
                first = head
            else:
                first.next = head.next
            head = head.next
        return first


if __name__ == '__main__':
    print("Testing linked lists")
    n1 = Node(5)
    LinkedListClass.add_node(n1, 5)
    LinkedListClass.add_node(n1, 6)
    LinkedListClass.add_node(n1, 7)
    LinkedListClass.add_node(n1, 8)
    LinkedListClass.add_node(n1, 9)

    LinkedListClass.print_linkedlist(n1)

    LinkedListClass.remove_duplicates(n1)
    LinkedListClass.print_linkedlist(n1)