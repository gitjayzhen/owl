import unittest

from algorithms.linkedlist import (
    reverse_list, reverse_list_recursive,
    is_sorted,
    remove_range,
    swap_pairs,
    rotate_right,
    is_cyclic,
    merge_two_list, merge_two_list_recur,
    is_palindrome, is_palindrome_stack, is_palindrome_dict,
    RandomListNode, copy_random_pointer_v1, copy_random_pointer_v2
)


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Convert from linked list Node to list for testing
def convert(head):
    ret = []
    if head:
        current = head
        while current:
            ret.append(current.val)
            current = current.next
    return ret


class TestSuite(unittest.TestCase):

    def setUp(self):
        # list test for palindrome
        a = Node('B')
        self.l = Node('A')
        self.l.next = a
        self.l.next.next = Node('C')
        self.l.next.next.next = Node('B')
        self.l.next.next.next.next = a

        self.l1 = Node('A')
        self.l1.next = Node('B')
        self.l1.next.next = Node('C')
        self.l1.next.next.next = Node('B')

    def test_reverse_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        self.assertEqual([4, 3, 2, 1], convert(reverse_list(head)))
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        self.assertEqual([4, 3, 2, 1], convert(reverse_list_recursive(head)))

    def test_is_sorted(self):
        head = Node(-2)
        head.next = Node(2)
        head.next.next = Node(2)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(9)
        # head -> -2 -> 2 -> 2 -> 4 -> 9
        self.assertTrue(is_sorted(head))
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(8)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(6)
        # head -> 1 -> 2 -> 8 -> 4 -> 6
        self.assertFalse(is_sorted(head))

    def test_remove_range(self):
        # Test case: middle case.
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        # Expect output: 0 4
        self.assertEqual([0, 4], convert(remove_range(head, 1, 3)))

        # Test case: taking out the front node
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        # Expect output: 2 3 4
        self.assertEqual([2, 3, 4], convert(remove_range(head, 0, 1)))

        # Test case: removing all the nodes
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        self.assertEqual([], convert(remove_range(head, 0, 7)))

    def test_swap_in_pairs(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        # Expect output : 2 --> 1 --> 4 --> 3
        self.assertEqual([2, 1, 4, 3], convert(swap_pairs(head)))

    def test_rotate_right(self):
        # Given 1->2->3->4->5->NULL
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        # K = 2. Expect output: 4->5->1->2->3->NULL.
        self.assertEqual([4, 5, 1, 2, 3], convert(rotate_right(head, 2)))

    def test_is_cyclic(self):
        # create linked list => A -> B -> C -> D -> E -> C
        head = Node('A')
        head.next = Node('B')
        curr = head.next
        cyclic_node = Node('C')
        curr.next = cyclic_node
        curr = curr.next
        curr.next = Node('D')
        curr = curr.next
        curr.next = Node('E')
        curr = curr.next
        curr.next = cyclic_node
        self.assertTrue(is_cyclic(head))

        # create linked list 1 -> 2 -> 3 -> 4
        head = Node(1)
        curr = head
        for i in range(2, 6):
            curr.next = Node(i)
            curr = curr.next
        self.assertFalse(is_cyclic(head))

    def test_merge_two_list(self):
        """
        Input: head1:1->2->4, head2: 1->3->4
        Output: 1->1->2->3->4->4
        """
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(4)
        head2 = Node(1)
        head2.next = Node(3)
        head2.next.next = Node(4)
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         convert(merge_two_list(head1, head2)))
        # Test recursive
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(4)
        head2 = Node(1)
        head2.next = Node(3)
        head2.next.next = Node(4)
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         convert(merge_two_list_recur(head1, head2)))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(self.l))
        self.assertFalse(is_palindrome(self.l1))

    def test_is_palindrome_stack(self):
        self.assertTrue(is_palindrome_stack(self.l))
        self.assertFalse(is_palindrome_stack(self.l1))

    def test_is_palindrome_dict(self):
        self.assertTrue(is_palindrome_dict(self.l))
        self.assertFalse(is_palindrome_dict(self.l1))

    def test_solution_0(self):
        self._init_random_list_nodes()
        result = copy_random_pointer_v1(self.random_list_node1)
        self._assert_is_a_copy(result)

    def test_solution_1(self):
        self._init_random_list_nodes()
        result = copy_random_pointer_v2(self.random_list_node1)
        self._assert_is_a_copy(result)

    def _assert_is_a_copy(self, result):
        self.assertEqual(5, result.next.next.next.next.label)
        self.assertEqual(4, result.next.next.next.label)
        self.assertEqual(3, result.next.next.label)
        self.assertEqual(2, result.next.label)
        self.assertEqual(1, result.label)
        self.assertEqual(3, result.next.next.next.next.random.label)
        self.assertIsNone(result.next.next.next.random)
        self.assertEqual(2, result.next.next.random.label)
        self.assertEqual(5, result.next.random.label)
        self.assertEqual(4, result.random.label)

    def _init_random_list_nodes(self):
        self.random_list_node1 = RandomListNode(1)
        random_list_node2 = RandomListNode(2)
        random_list_node3 = RandomListNode(3)
        random_list_node4 = RandomListNode(4)
        random_list_node5 = RandomListNode(5)

        self.random_list_node1.next, self.random_list_node1.random = random_list_node2, random_list_node4
        random_list_node2.next, random_list_node2.random = random_list_node3, random_list_node5
        random_list_node3.next, random_list_node3.random = random_list_node4, random_list_node2
        random_list_node4.next = random_list_node5
        random_list_node5.random = random_list_node3

    def test_select_head(self):
        """给定一个链表环，返回一个环的入口节点，如果没有环，就返回null？ 能否给出不利用额外空间的解法吗 ? 这个结构就是Q或L

        从链表起始处到环入口长度为：a，从环入口到Faster和Slower相遇点长度为：x，整个环长为：c。
        假设从开始到相遇，Slower走过的路程长为s，由于Faster的步速是Slower的2倍，那么Faster在这段时间走的路程长为2s。
        而对于Faster来说，他走的路程还等于之前绕整个环跑的n圈的路程nc，加上最后这一次遇见Slower的路程s。

        2s = nc + s

        对于Slower来说，他走的路程长度s还等于他从链表起始处到相遇点的距离，所以有：
        s = a + x
        简化
                a + x = nc

                a = nc - x

                a = (n-1)c + c-x

                a = kc + (c-x)

        """

        if self.l is None or self.l.next is None:
            return None

        slow = self.l
        fast = self.l

        while True:
            if slow is None or fast is None:
                return None

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        slow = self.l
        while slow != fast:
            slow = slow.next
            fast = fast.next

        print(slow.val)

    def test_select_head2(self):
        head = self.l
        head.__setattr__('mark', 1)
        while True:
            head = head.next
            if head is None or head.next is None:
                break
            if hasattr(head, 'mark'):
                head.__setattr__('mark', getattr(head, "mark") + 1)
                if getattr(head, "mark") > 1:
                    print(head.val)
                    return
            head.__setattr__('mark', 1)



if __name__ == "__main__":
    unittest.main()


