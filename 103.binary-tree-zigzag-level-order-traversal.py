# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.helper(root,0)
        return self.res
    def helper(self,root,level):
        if not root: return
        if len(self.res) <= level:
            self.res.append([])
        if level % 2 == 1:
            self.res[level].insert(0,root.val)
        else:
            self.res[level].append(root.val)
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)
                
    
