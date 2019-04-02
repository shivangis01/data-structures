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

    @staticmethod
    def return_last_node(node, count):
        """

        :param node:
        :param count:
        :return:
        """
        if node is None:
            return
        while node.next is not None:
            return LinkedListClass.return_last_node(node.next, count)

    @staticmethod
    def kth_to_last_node_recursive(head: Node, k: int):
        """
        Recursively look for the kth to last node of a given linked list

        Time Complexity: O(n)
        Space Complexity: O(n)

        :param head: linked list head
        :param k:
        :return: Value of kth-to-last node
        """
        if head is None:
            return 0
        i = LinkedListClass.kth_to_last_node_recursive(head.next, k) + 1
        if k == i:
            print("The kth node is : {}".format(head.val))
        return i

    @staticmethod
    def kth_to_last_node_iterative(head: Node, k: int) -> Node:
        """
        Iterates to look for the kth to last node of a given linked list, uses 2 pointers

        Time Complexity: O(n)
        Space Complexity: O(1)

        :param head:
        :param k:
        :return:
        """
        p1 = head
        p2 = head
        count = 0

        # Move p2 k nodes apart from p1
        while count != k:
            p2 = p2.next
            count += 1

        # Move both p1 & p2 until p2 reaches the end
        while p2 is not None:
            p2 = p2.next
            p1 = p1.next

        return p1

    @staticmethod
    def delete_middle_node(head: Node):
        """
        Delete a middle node from a linked list given access to only that node

        :param head:
        :return:
        """
        if head is None or head.next is None:
            return False
        next_node = head.next
        head.val = next_node.val
        head.next = next_node.next
        return True

    @staticmethod
    def partition_linked_list(head: Node, partition: int):
        l1 = Node(0)
        l1_start = l1
        l2 = Node(0)
        l2_start = l2
        while head is not None:
            if head.val < partition:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = None
        l2.next = None

        new_head = l1_start.next
        while l1.next is not None:
            l1 = l1.next
        l1.next = l2_start.next
        return new_head

    @staticmethod
    def sum_linked_lists(h1: Node, h2: Node):
        """
        Assuming digits are stored in reverse order (617 is 6 -> 1 -> 7), calculate sum of all digits
        :param h1:
        :param h2:
        :return:
        """
        if h1 is None or (h1.val and h1.next is None):
            return h2
        if h2 is None or (h2.val and h2.next is None):
            return h1

        sum_list = Node(0)
        sum_list_head = sum_list
        carry = 0
        while h1 is not None and h2 is not None:
            sum_value = int((h1.val + h2.val + carry) % 10)
            carry = int((h1.val + h2.val + carry) / 10)
            sum_list.next = Node(sum_value)
            h1 = h1.next
            h2 = h2.next
            sum_list = sum_list.next

        if h1 is None:
            sum_list.next = h2

        if h2 is None:
            sum_list.next = h1

        if carry:
            sum_list.next = Node(carry)

        return sum_list_head.next


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

    k = 3
    LinkedListClass.kth_to_last_node_recursive(n2, k)
    print("{}th to last node is {}".format(k, LinkedListClass.kth_to_last_node_iterative(n2, k).val))

    LinkedListClass.delete_middle_node(n2.next.next)
    LinkedListClass.print_linkedlist(n2)

    n3 = Node(10)
    LinkedListClass.add_node(n3, 5)
    LinkedListClass.add_node(n3, 2)
    LinkedListClass.add_node(n3, 7)
    LinkedListClass.add_node(n3, 1)
    LinkedListClass.add_node(n3, 9)
    LinkedListClass.print_linkedlist(n3)
    new = LinkedListClass.partition_linked_list(n3, 5)
    print("Partitioning linked list around the value {}".format(5))
    LinkedListClass.print_linkedlist(new)

    h1 = Node(1)
    LinkedListClass.add_node(h1, 5)
    LinkedListClass.add_node(h1, 6)
    print("h1:")
    LinkedListClass.print_linkedlist(h1)

    h2 = Node(4)
    LinkedListClass.add_node(h2, 5)
    LinkedListClass.add_node(h2, 6)
    print("h2:")
    LinkedListClass.print_linkedlist(h2)

    sum = LinkedListClass.sum_linked_lists(h1, h2)
    print("Sum of two lists is:")
    LinkedListClass.print_linkedlist(sum)
