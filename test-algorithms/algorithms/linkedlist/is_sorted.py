"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.

给定一个链表，如果链表是有序的，is_sort函数返回真
(递增)顺序，否则返回false。考虑空列表
待分类。

For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""


def is_sorted(head):
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True
