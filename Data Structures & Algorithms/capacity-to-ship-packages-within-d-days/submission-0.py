class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        ans = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if self.canShip(mid, weights, days):
                high = mid - 1
                ans = min(ans, mid)
            else:
                low = mid + 1
        
        return ans

            
    def canShip(self, mid, weights, days):
        used_days = 1
        remaining = mid
    
        for w in weights:        
            if remaining < w:
                remaining = mid
                used_days += 1
            
            remaining -= w
        
        if used_days > days:
            return False
        else:
            return True
        