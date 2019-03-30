# -*- coding: utf-8 -*-
import linked_list
from linked_list import LinkedNode

def reverse(llist):
    cur, prev = llist, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

def reverse_linked_list(head):
    cur, prev = head, None
    while cur:
        tail = cur.next
        cur.next = prev
        prev = cur
        cur = tail
    return prev

if __name__ == '__main__':
    llist = linked_list.init_llist([1,2,3,4])
    #rlist = reverse(llist)
    rlist = reverse_linked_list(llist)
    linked_list.print_llist(rlist)
