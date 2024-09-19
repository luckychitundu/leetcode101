from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = Counter(nums) 
        for k, v in mapping.items():
            if v == 1:
                return k 

        