# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.preorder(root,"")
        return self.res
        
    def preorder(self,root,pre):
        if not root: return
        pre = pre+str(root.val)
        if not root.left and not root.right:
            self.res.append(pre)
        self.preorder(root.left,pre+"->")
        self.preorder(root.right,pre+"->")
