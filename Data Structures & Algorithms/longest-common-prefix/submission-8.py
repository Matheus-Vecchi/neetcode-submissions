class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = strs[0]

        for s in range(len(strs)):
            if len(strs[s]) < len(shortest_str):
                shortest_str = strs[s]
        ii = 0
        while ii < len(shortest_str):
            i = 1
            while i < len(strs):
                if strs[0][ii] != strs[i][ii]:
                    return strs[0][0:ii]
                
                i += 1

            ii += 1
        
        return shortest_str
    