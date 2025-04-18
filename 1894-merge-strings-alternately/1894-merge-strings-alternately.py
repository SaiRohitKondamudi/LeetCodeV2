class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxlen = max(len(word1), len(word2))
        result = []
        
        for i in range(maxlen):
            if i< len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        
        return "".join(result)
            
            