# -*- coding: utf-8 -*-
import linked_list
from linked_list import LinkedNode

def bubble_sort_linked_list(head):
    cur, tail, tmp_head = head, None, LinkedNode(-1)
    pre, pre.next = tmp_head, head
    while tail != tmp_head.next:
        while cur.next != tail:
            if cur.value > cur.next.value:
                a = pre.next
                b = pre.next.next
                pre.next, b.next, a.next = b, a, b.next
            pre = pre.next
            cur = pre.next
        tail = pre
        cur = tmp_head.next
        pre = tmp_head
    return tmp_head.next

if __name__ == "__main__":
    head = linked_list.init_llist([21, 25, 49, 25, 16, 8])
    linked_list.print_llist(head)
    head = bubble_sort_linked_list(head)
    linked_list.print_llist(head)
