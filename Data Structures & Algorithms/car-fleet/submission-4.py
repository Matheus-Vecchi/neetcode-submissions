class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        aux = []
        cars = list(zip(position, speed))
        cars = sorted(cars)
        stack = []

        for pos, speed in cars:
            aux.append((target - pos) / speed)

        for i in aux:
            while stack and i >= stack[-1]:
                stack.pop()
            stack.append(i)

        return len(stack)