# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.helper(root,[],0,sum)
        return self.res
    def helper(self,root,temp,tot,sum):
        if not root: return
        temp = temp + [root.val]
        tot = tot + root.val
        if not root.left and not root.right and tot == sum:
            self.res.append(temp)

        self.helper(root.left,temp,tot,sum)
        self.helper(root.right,temp,tot,sum)
