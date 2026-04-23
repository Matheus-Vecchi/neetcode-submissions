class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        i = 0
        ans = 1

        for r in range(1, len(arr)):
            if arr[r] > arr[i]:
                current = 1
            elif arr[r] < arr[i]:
                current = 0
            else:
                l = r
                current = -1
            
            if r > 1 and current != -1:
                if current == previous:
                    l = i
            
            previous = current

            i += 1

            ans = max(r - l + 1, ans)

        return ans
