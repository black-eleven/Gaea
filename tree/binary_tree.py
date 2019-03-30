# -*- coding: utf-8 -*-

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def init_tree(l):
    root = BinaryTreeNode(l[0])
    node_queue = []
    node_queue.append(root)
    i = 1
    while i < len(l):
        node = node_queue.pop()
        left_node = BinaryTreeNode(l[i])
        i += 1
        node.left = left_node
        node_queue.insert(0, left_node)
        right_node = BinaryTreeNode(l[i])
        node.right = right_node
        node_queue.insert(0, right_node)
        i += 1
    return root

def preorder(root):
    if not root:
        return
    print root.value,
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.value,
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.value,

if __name__ == "__main__":
    root = init_tree([1,2,3,4,5,6,7,8,9])
    preorder(root)
    print
    inorder(root)
    print
    postorder(root)
