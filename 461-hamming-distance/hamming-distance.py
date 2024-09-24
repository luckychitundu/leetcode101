class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0 
        v = x ^ y 
        v = bin(v)[2:] 
        for i in range(len(v)):
            if v[i] == "1":
                count += 1 
        return count         



        