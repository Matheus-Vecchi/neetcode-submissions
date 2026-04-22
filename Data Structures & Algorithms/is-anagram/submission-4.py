class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        for i in range(0, len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1

            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        
        for k, v in dict_s.items():
            if k not in dict_t:
                return False
            else:
                if dict_s[k] != dict_t[k]:
                    return False
        
        return True