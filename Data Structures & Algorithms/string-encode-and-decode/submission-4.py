class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for pos, i in enumerate(strs):
            encoded += str(len(i)) + "é" + i
        
        return encoded

    def decode(self, s: str) -> List[str]:
        j = 0
        t = 0
        strs = []

        while j < len(s):
            if s[j] == "é":
                last_char = int(s[t:j])
                strs.append(s[j+1:j+1+last_char])
                j += last_char
                t = j + 1
            j += 1
        
        return strs