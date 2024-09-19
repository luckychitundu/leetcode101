class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(1, n):
            if (int(s[i]) % 2 == 0 and int(s[i-1]) % 2 == 0) or (int(s[i]) % 2 == 1 and int(s[i-1]) % 2 == 1):
                if int(s[i]) < int(s[i-1]):  
                    s = s[:i-1] + s[i] + s[i-1] + s[i+1:]
                    break     
        return s             



        