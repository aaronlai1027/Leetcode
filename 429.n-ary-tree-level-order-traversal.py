"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res = []
        self.helper(root,0)
        return self.res
    def helper(self,root,level):
        if not root:
            return
        if level == len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        for child in root.children:
            self.helper(child,level+1)
