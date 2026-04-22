class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer].isalnum() is False and s[right_pointer].isalnum():
                left_pointer += 1
            elif s[left_pointer].isalnum() and s[right_pointer].isalnum() is False:
                right_pointer -= 1
            elif s[left_pointer].isalnum() is False and s[right_pointer].isalnum() is False:
                left_pointer += 1
                right_pointer -= 1
            else:
                if s[left_pointer] != s[right_pointer]:
                    return False
                left_pointer += 1
                right_pointer -= 1

        return True