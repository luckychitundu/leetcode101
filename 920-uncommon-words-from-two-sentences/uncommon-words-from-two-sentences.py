from collections import Counter 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1, s2 = s1.split(), s2.split() 
        words = s1 + s2 
        mapping = Counter(words) 
        for k, v in mapping.items():
            if v == 1:
                res.append(k) 
        return res         

