# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA and headB:
        #     A, B = headA, headB
        #     while A!=B:
        #         A = A.next if A else headB
        #         B = B.next if B else headA
        #     return A
        if headA is None or headB is None:
            return None
        A = headA
        B = headB
        
        while A is not B:
            A = headB if A is None else A.next
            B = headA if B is None else B.next
            
        return A
