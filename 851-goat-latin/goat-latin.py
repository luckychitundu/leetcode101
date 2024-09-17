class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] 
        words = sentence.split() 
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word = word + "ma" + "a" * (i + 1)
                words[i] = word 
            else:
                word = word[1:] + word[0] + "ma" + "a" * (i + 1)
                words[i] = word 
        return " ".join(words)         