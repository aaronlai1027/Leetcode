# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        map = {}
        return self.dfs(root,map)
        
    def dfs(self,root,map):
        if not root:
            return 0
        if root in map:
            return map[root]
        val = 0
        if root.left:
            val+=self.dfs(root.left.left,map)+self.dfs(root.left.right,map)
        if root.right:
            val+=self.dfs(root.right.left,map)+self.dfs(root.right.right,map)
         
        val = max(root.val+val,self.dfs(root.left,map)+self.dfs(root.right,map))
        map[root] = val
        return val
