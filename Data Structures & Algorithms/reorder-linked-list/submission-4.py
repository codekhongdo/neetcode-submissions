# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack=[]
        curr=head
        while curr is not None:
            stack.append(curr)
            curr=curr.next
        curr=head
        n=len(stack)
        for i in range(n//2):
            A=stack.pop()
            temp=curr.next
            A.next=temp
            curr.next=A
            curr=temp
        curr.next=None
        

        