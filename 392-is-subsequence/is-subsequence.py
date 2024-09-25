class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t) 
        i = 0
        j = 0 
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1 
                j += 1 
            else:
                j += 1 
        return i == n             
        

        