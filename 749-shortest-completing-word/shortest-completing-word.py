from collections import Counter 
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hashMap = {}
        for char in licensePlate:
            if char.isalpha():
                letter = char.casefold()
                hashMap[letter] = hashMap.get(letter, 0) + 1
        valid_words = []
        for word in words:
            local_mapping = Counter(word)
            if all(local_mapping.get(k, 0) >= hashMap[k] for k in hashMap):
                valid_words.append(word)

        return min(valid_words, key=len)
