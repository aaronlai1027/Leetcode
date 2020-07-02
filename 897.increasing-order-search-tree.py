# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = TreeNode(0)
        self.pre = res
        self.helper(root)
        return res.right
        
    def helper(self,root):
        if not root:
            return 
        self.helper(root.left)
        root.left = None
        self.pre.right = root
        self.pre = root
        self.helper(root.right)
#     def increasingBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         dummy = TreeNode(-1)
#         self.prev = dummy
#         self.inOrder(root)
#         return dummy.right
        
#     def inOrder(self, root):
#         if not root:
#             return None
#         self.inOrder(root.left)
#         root.left = None
#         self.prev.right = root
#         self.prev = self.prev.right
#         self.inOrder(root.right)
