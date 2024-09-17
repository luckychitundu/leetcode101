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
            return head
        
        # Use a stack to store the nodes we need to visit later (when we're done with the child)
        stack = []
        curr = head
        
        while curr:
            if curr.child:
                # If the current node has a child, we'll push the next node onto the stack (if it exists)
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None  # Detach it for now
                
                # Then, we link the current node to its child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None  # Clear the child pointer after flattening
            elif not curr.next and stack:
                # If we're at the end of the current list but have stored nodes on the stack
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr
            
            # Move to the next node
            curr = curr.next
        
        return head
