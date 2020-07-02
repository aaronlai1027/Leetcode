"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = tmp = Node()
        dummy = root
        while root:
            if root.left:
                cur.next = root.left
                cur = root.left
            if root.right:
                cur.next = root.right
                cur = root.right
            if root.next:
                root = root.next
            else:
                root = tmp.next
                cur = tmp = Node()    
        return dummy
