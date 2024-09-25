class Solution:
    def maxDepth(self, s: str) -> int:
        # Input: s = "(1+(2*3)+((8)/4))+1" 
        # Input: s = "(1)+((2))+(((3)))" 
        stack = [] 
        max_depth = 0 
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
                current_depth = len(stack) 
                max_depth = max(max_depth, current_depth) 
            elif s[i] == ")":
                stack.pop() 
        return max_depth          
                
        