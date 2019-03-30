# -*- coding: utf-8 -*-

from binary_tree import BinaryTreeNode, postorder

def rebuild_tree(preorder, prestart, inorder, instart, inend):
    print preorder, prestart, inorder, instart, inend
    if instart > inend:
        return None
    node = BinaryTreeNode(preorder[prestart])
    if instart == inend:
        return node
    in_index = findindex(inorder, instart, inend, preorder[prestart])
    print in_index
    if prestart + 1 > len(preorder):
        return node
    node.left = rebuild_tree(preorder, prestart+1, inorder, instart, in_index-1)
    if in_index + 1 > len(preorder):
        return node
    node.right = rebuild_tree(preorder, in_index+1, inorder, in_index+1, inend)
    return node

def findindex(l, start, end, target):
    for i in range(start, end+1):
        if l[i] == target:
            return i
    return -1

if __name__ == "__main__":
    root = rebuild_tree([1, 2, 4, 8, 9, 5, 3, 6, 7], 0, [8, 4, 9, 2, 5, 1, 6, 3, 7], 0, 8)
    postorder(root)
