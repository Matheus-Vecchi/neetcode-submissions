class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True