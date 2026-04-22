class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for current in asteroids:
            alive = True

            while alive and stack and current < 0 and stack[-1] > 0:
                if current + stack[-1] == 0:
                    stack.pop()
                    alive = False
                elif abs(int(current)) > abs(int(stack[-1])):
                    stack.pop()
                elif abs(int(current)) < abs(int(stack[-1])):
                    alive = False
            
            if alive:
                stack.append(current)

        return stack