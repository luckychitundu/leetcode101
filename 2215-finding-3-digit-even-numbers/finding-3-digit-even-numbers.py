class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        for i in range(len(digits)):
            if digits[i] == 0:
                continue 
            for j in range(len(digits)):
                if j == i:
                    continue 
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue 
                    if digits[k] % 2 == 0:
                        num = str(digits[i]) + str(digits[j]) + str(digits[k]) 
                        res.append(int(num))  
        return sorted(set(res))                


