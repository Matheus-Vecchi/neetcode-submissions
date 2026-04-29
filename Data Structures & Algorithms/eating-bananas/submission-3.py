class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.h = h
        self.piles = piles
        
        lowest = 1
        highest = max(piles)
    
        self.ans = max(piles)

        while lowest <= highest:
            mid = (highest + lowest) // 2

            if self.aux(mid) > self.h:
                lowest = mid + 1
            elif self.aux(mid) <= self.h:
                highest = mid - 1
                self.ans = min(self.ans, mid)
        
        return self.ans


    def aux(self, x):
        hours_eaten = 0

        for i in self.piles:
            hours_eaten += (i + x - 1) // x

        return hours_eaten
