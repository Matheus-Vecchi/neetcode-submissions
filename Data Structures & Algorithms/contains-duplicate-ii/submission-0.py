class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for pos, i in enumerate(nums):
            if i not in hashmap:
                hashmap[i] = [pos]
            else:
                hashmap[i].append(pos)

        for key in hashmap.keys():
            l = 0
            r = 1

            while r < len(hashmap[key]):
                if hashmap[key][r] - hashmap[key][l] <= k:
                    return True
                else:
                    l += 1
                    r += 1
        
        return False
        