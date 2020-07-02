# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root,res,0)
        return res
    
    def level(self,root,res,level):
        if root:
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            self.level(root.left,res,level+1)
            self.level(root.right,res,level+1)
