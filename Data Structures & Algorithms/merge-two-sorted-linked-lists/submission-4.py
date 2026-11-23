# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        start=ListNode()
        p=start
        while (p1 is not None) and (p2 is not None):
            if p1.val<=p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            p=p.next
        p.next=p1 if p1 is not None else p2
        
        return start.next