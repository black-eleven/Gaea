# -*- coding: utf-8 -*-

class LinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def init_llist(_list):
    rlist = LinkedNode(_list[0])
    cur_node = rlist
    for element in _list[1:]:
        node = LinkedNode(element)
        cur_node.next = node
        cur_node = cur_node.next
    return rlist

def print_llist(llist):
    while llist:
        print llist.value,
        llist = llist.next
    print ""
