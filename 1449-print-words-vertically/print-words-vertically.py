class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split() 
        max_len = len(max(s, key=len))
        print(max_len)
        s = [word + " " * (max_len - len(word)) for word in s]
        print(s)
        mapping = {}
        for i in range(len(s)):
            for j in range(len(s[i])):
                if j not in mapping:
                    mapping[j] = s[i][j]   
                else:
                    mapping[j] += s[i][j] 

        new_list = list(mapping.values())    

        new_list = [word.rstrip() for word in new_list]        
        print(new_list)      
        return new_list           

        