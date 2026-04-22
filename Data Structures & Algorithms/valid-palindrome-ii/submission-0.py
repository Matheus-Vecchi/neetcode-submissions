class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                if self.aux(l + 1, r, s):
                    return self.aux(l + 1, r, s)
                else:
                    return self.aux(l, r - 1, s)
            l += 1
            r -= 1

        return True
                

    def aux(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

