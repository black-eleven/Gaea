# -*- coding: utf-8 -*-
import linked_list

def delet_countdown_element(head, k):
    slow = head
    fast = head
    for i in range(k):
        fast = fast.next
    prev = None
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next
    prev.next = slow.next

if __name__ == "__main__":
    llist = linked_list.init_llist([1,2,3,4])
    delet_countdown_element(llist, 3)
    linked_list.print_llist(llist)
