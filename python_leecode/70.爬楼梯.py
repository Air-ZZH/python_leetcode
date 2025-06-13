class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a = 1;
        b = 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

#经典的动态规划（Dynamic Programming）入门题
# f(n) = f(n-1) + f(n-2)