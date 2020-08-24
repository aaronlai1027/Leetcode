# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        res = head
        tot = 0
        while l1 or l2:
            tot = tot // 10
            if l1:
                tot += l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next
                
            res.next = ListNode(tot % 10)
            res = res.next
        if tot >= 10:
            res.next = ListNode(1)
        return head.next