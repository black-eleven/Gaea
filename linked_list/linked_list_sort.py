# -*- coding: utf-8 -*-
import linked_list

def merge_sort_list(head):
    if not head or not head.next:
        return head
    fast, slow = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    #tmp = slow
    #slow = slow.next
    #tmp.next = None
    tmp = slow.next
    slow.next = None
    prev = merge_sort_list(head)
    #after = merge_sort_list(slow)
    after = merge_sort_list(tmp)
    return merge(prev, after)

def merge(head1, head2):
    ret, p = None, None
    if head1.value < head2.value:
        ret = head1
        head1 = head1.next
    else:
        ret = head2
        head2 = head2.next

    p = ret
    while head1 and head2:
        if head1.value < head2.value:
            p.next = head1
            head1 = head1.next
        else:
            p.next = head2
            head2 = head2.next
        p = p.next

    if head1:
        p.next = head1
    if head2:
        p.next = head2
    return ret

if __name__ == "__main__":
    head = linked_list.init_llist([21, 25, 49, 25, 16, 8])
    linked_list.print_llist(head)
    head = merge_sort_list(head)
    linked_list.print_llist(head)
