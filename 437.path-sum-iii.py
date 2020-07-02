# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.pathnum = 0
        self.dfs(root,sum)
        return self.pathnum
        
    def dfs(self, node, sum):
        if not node:
            return
        self.dfs2(node,sum)
        self.dfs(node.left,sum)
        self.dfs(node.right,sum)
        
    def dfs2(self, node, sum):
        if not node:
            return
        if node.val == sum:
            self.pathnum += 1
        self.dfs2(node.left, sum - node.val)
        self.dfs2(node.right, sum - node.val)
