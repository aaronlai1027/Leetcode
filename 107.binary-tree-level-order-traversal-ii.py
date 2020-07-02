# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque([(root,0)])
        res = []
        # q.append((root,0))
        while q:
            node, level = q.popleft()
            if node:
                if len(res) < level +1:
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                q.append((node.left,level+1))
                q.append((node.right,level+1))
        return res
        
