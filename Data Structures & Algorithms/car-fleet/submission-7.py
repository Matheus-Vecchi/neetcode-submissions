class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = []
        velo = []

        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr = sorted(arr, key=lambda x: x[0], reverse=False)

        for i in range(len(arr)):
            car_velo = (target - arr[i][0]) / arr[i][1]
            velo.append(car_velo)

        for i in velo:
            while stack and i >= stack[-1]:
                stack.pop()
            stack.append(i)

        return len(stack)

        #0, 1, 4, 7
        #10, 4.5, 3, 3
