# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        self.helper(root,L,R)
        return self.sum
    
    def helper(self,root,L,R):
        if not root:
            return
        if root.val >= L and root.val<= R:
            self.sum += root.val
        self.helper(root.left,L,R)
        self.helper(root.right,L,R)
