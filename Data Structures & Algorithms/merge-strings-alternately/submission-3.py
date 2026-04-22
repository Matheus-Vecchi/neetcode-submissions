class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        c = 0

        ans = ""
        
        while c < len(word1 + word2):
                if i < len(word1):
                        ans += word1[i]
                        i += 1
                        c += 1

                if j < len(word2):
                        ans += word2[j]
                        j += 1
                        c += 1

        return ans