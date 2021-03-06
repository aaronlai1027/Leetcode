"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxd = 0
        for child in root.children:
            maxd = max(maxd,self.maxDepth(child))
        return maxd+1
