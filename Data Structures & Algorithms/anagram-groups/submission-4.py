class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for anagram in strs:
            temp = anagram
            temp = "".join(sorted(temp))
            if temp not in hashmap:
                hashmap[temp] = [anagram]
            else:
                hashmap[temp].append(anagram)

        ans = []

        for v in hashmap.values():
            ans.append(v)
        
        return ans