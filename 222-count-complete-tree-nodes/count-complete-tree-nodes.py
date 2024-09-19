# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        stack = [root] 
        count = 0 
        while stack:
            node = stack.pop() 
            count += 1 
            if node.right:
                stack.append(node.right) 
            if node.left:
                stack.append(node.left) 
        return count              

