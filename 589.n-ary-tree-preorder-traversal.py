"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root:
            return
        self.res.append(root.val)
        for child in root.children:
            self.helper(child)
