# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = []
        self.helper(root,k)
        return self.res[k-1]
    def helper(self,root,k):
        if not root: return
        self.helper(root.left,k)
        self.res.append(root.val)
        if len(self.res) == k:
            return
        
        self.helper(root.right,k)
