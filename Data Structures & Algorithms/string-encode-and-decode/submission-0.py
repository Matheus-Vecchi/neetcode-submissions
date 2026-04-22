class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for pos, c in enumerate(strs):
            encoded_string += str(len(strs[pos])) + "#" + c
        return encoded_string
    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        j = 0

        while j <= len(s) - 1:
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            strs.append(s[j+1 : j+1+length])
            i = j + 1 + length
            j = i
        return strs
            