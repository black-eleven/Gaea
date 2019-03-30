# -*- coding: utf-8 -*-
import linked_list

def exchange_element(head, n):
    cur, prev = head, None
    i = 0
    while cur:
        i+=1
        prev = cur
        cur = cur.next
        if i == n:
            break
    if not cur:
        return "cannot find element"
    #tail = cur.next
    #tmp = cur.next
    #cur.next = tail.next
    #prev.next = tail
    #tail.next = cur
    a = cur.next
    b = cur.next.next
    a.next = cur
    cur.next = b
    prev.next = a

if __name__ == "__main__":
    llist = linked_list.init_llist([1,2,3,4])
    exchange_element(llist, 1)
    linked_list.print_llist(llist)
