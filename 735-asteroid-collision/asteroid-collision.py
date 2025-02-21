class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stable = list()
        for asteroid in asteroids:
            while stable and asteroid < 0 < stable[-1]:
                if stable[-1] < -asteroid:
                    stable.pop()
                    continue
                elif stable[-1] == -asteroid:
                    stable.pop()
                break
            else:
                stable.append(asteroid)
        return stable
                