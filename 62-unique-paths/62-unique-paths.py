class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(val):
            fact = 1
            for i in range(2, val+1):
                fact *= i
            return fact
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
        