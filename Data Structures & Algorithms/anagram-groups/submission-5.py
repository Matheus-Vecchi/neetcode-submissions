class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for an in strs:
            srt_an = tuple(sorted(an))

            if srt_an not in hashmap:
                hashmap[srt_an] = [an]
            else:
                hashmap[srt_an].append(an)
        
        return list(hashmap.values())