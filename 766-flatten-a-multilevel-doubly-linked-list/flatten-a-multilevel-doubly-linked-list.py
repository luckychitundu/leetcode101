"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        temp = []         
        curr = head 
        while curr:
            if curr.child:
                if curr.next:
                    temp.append(curr.next)
                    curr.next.prev = None

                curr.next = curr.child 
                curr.child.prev = curr 
                curr.child = None 
            elif not curr.next and temp:
                node = temp.pop() 
                curr.next = node 
                node.prev = curr     
            curr = curr.next    
        
        return head          
               
