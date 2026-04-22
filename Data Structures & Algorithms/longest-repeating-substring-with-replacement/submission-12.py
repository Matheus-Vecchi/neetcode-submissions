class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        dominant_char = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            
            dominant_char = max(hashmap[s[r]], dominant_char)

            while r - l + 1 - dominant_char > k:
                hashmap[s[l]] -= 1
                l += 1
            
            ans = max(r - l + 1, ans)
        
        return ans