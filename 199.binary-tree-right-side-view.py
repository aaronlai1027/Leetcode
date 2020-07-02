# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = [-1]
        self.helper(root,0)
        return self.res
    def helper(self,root,level):
        if not root: return
        if len(self.res) <= level:
            self.res.append([-1])
        self.res[level] = root.val
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)

