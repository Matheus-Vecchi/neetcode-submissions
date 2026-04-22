class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]
        for i in strs:
            if len(i) < len(smallest):
                smallest = i
        
        i = 0
        j = 1
        char = 0

        while char < len(smallest):
            while j < len(strs):
                if strs[i][char] != strs[j][char]:
                    return strs[i][0:char]

                j += 1

            j = 1
            char += 1
        
        return smallest

