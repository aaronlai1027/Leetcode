# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q: return p == q
        if p.val != q.val: return False
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)
        return l and r
