class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        aux = []
        cars = list(zip(position, speed))
        cars = sorted(cars)
        stack = []
        ans = len(position)

        for pos, speed in cars:
            aux.append((target - pos) / speed)

        for i in aux:
            while stack and i >= stack[-1]:
                stack.pop()
                ans -= 1
            stack.append(i)

        return ans