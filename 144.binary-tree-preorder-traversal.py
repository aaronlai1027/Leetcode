# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.preorder(root)
        return self.res
    def preorder(self,root):
        if not root:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
