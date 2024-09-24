class Solution:
    def getLenCommon(self, pair1, pair2):
        pair1, pair2 = str(pair1), str(pair2) 
        if len(pair1) > len(pair2):
            n = len(pair2)
        else:
            n = len(pair1) 
        count = 0
        for i in range(n):
            if pair1[i] != pair2[i]:
                break 
            else:
                count += 1     
        return count        
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_len = 0 
        d1 = sorted(map(str, set(arr1)))
        d2 = sorted(map(str, set(arr2)))
        i = j = 0 
        while i <len(d1) and j < len(d2):
            max_len = max(max_len, self.getLenCommon(d1[i], d2[j]))
            if d1[i] < d2[j]:
                i += 1
            else:
                j += 1 
        return max_len             

