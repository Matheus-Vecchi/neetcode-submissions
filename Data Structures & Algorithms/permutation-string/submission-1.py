class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        cur = {}

        for i in s1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        l = 0
        
        for r in range(len(s2)):
            if s2[r] in cur:
                cur[s2[r]] += 1
            else:
                cur[s2[r]] = 1
            
            if cur == hashmap:
                return True
            
            if r - l + 1 == len(s1):
                if cur[s2[l]] == 1:
                    cur.pop(s2[l])
                else:
                    cur[s2[l]] -= 1
                l += 1
        
        return False