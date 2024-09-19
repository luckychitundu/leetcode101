# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get size of list
        # middle = size//2 
        # 5//2 = 2 + 1 ....6//2=3+1
        # for a 1-indexed list, the middle index = (size//2) + 1
        size = 0
        if not head:
            return size 
        current = head 
        while current:
            size += 1 
            current = current.next 
        mid = (size//2) + 1 

        current = head 
        while current and mid > 1:
            mid -= 1 
            current = current.next 
        return current     








        