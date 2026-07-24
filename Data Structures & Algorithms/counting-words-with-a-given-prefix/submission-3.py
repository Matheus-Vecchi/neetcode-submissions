class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        end = len(pref)
        count = 0

        for word in words:
            if word[:end] == pref:
                count += 1

        return count