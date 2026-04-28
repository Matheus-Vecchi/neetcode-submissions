class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}

        ans = {}

        for i in s1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        l = 0

        for r in range(len(s2)):
            if s2[r] in ans:
                ans[s2[r]] += 1
            else:
                ans[s2[r]] = 1

            if r - l + 1 == len(s1):
                if ans == hashmap:
                    return True
                if ans[s2[l]] == 1:
                    ans.pop(s2[l])
                else:
                    ans[s2[l]] -= 1
                l += 1

        return False