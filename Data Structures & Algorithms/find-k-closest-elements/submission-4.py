class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - k

        while low < high:
            mid = (low + high) // 2

            if abs(arr[mid] - x) <= abs(arr[mid+k] - x):
                high = mid
            else:
                low = mid + 1
        
        return arr[low:low+k]