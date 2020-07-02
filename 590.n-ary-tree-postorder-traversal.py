"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
        
    def helper(self,root):
        if not root:
            return
        for child in root.children:
            self.helper(child)
        self.res.append(root.val)
