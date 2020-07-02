# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverse(head)
    
    def _reverse(self, node, prev = None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self._reverse(next, node)
