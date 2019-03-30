# -*- coding: utf-8 -*-
import linked_list

def judge_ring(head):
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

if __name__ == "__main__":
    llist = linked_list.init_llist([1,2,3,4])
    print judge_ring(llist)
