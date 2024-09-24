class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2) 
        c = a + b
        return bin(c)[2:]
        