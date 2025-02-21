class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stable = [asteroids[0]]
        for i in range(1, len(asteroids)):
            asteroid = asteroids[i]
            if asteroid < 0:
                stable = self.collide(stable, asteroid)
            else:
                stable.append(asteroid)
        return stable

    def collide(self, stable, asteroid):
        asteroid_size = abs(asteroid)
        for i in range(len(stable)-1, -1, -1):
            if stable[i] < 0:
                return stable[:i+1] + [asteroid]
            elif stable[i] > asteroid_size:
                return stable[:i+1]
            elif stable[i] == asteroid_size:
                return stable[:i]
            else:
                pass
        return [asteroid]
                
        return stable