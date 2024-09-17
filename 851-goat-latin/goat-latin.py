class Solution:
    def toGoatLatin(self, sentence: str) -> str: 
        words = sentence.split() 
        for i in range(len(words)):
            word = words[i]
            if word[0].casefold() in "aeiou":
                word = word + "ma" + "a" * (i + 1)
                words[i] = word 
            else:
                word = word[1:] + word[0] + "ma" + "a" * (i + 1)
                words[i] = word 
        return " ".join(words)         