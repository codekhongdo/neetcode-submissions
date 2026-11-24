# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.memo=set()
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point=head
        while point !=None:
            point=point.next
            if point in self.memo:
                return True
            self.memo.add(point)
        return False

        