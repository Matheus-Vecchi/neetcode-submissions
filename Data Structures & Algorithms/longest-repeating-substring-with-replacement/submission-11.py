class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        ans = 0
        max_freq = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            
            max_freq = max(max_freq, hashmap[s[r]])

            while r - l + 1 - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            
            ans = max(r - l + 1, ans)
        
        return ans