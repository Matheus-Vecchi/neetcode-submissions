class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        ans = low

        while low <= high:
            mid = (high + low) // 2

            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
                ans = max(ans, mid)
            else:
                return mid
        
        return ans