class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

    # 如果是偶数位，x 应该等于 reversed_half
    # 如果是奇数位，x 应该等于 reversed_half // 10（中间的数字无关）
        return x == reversed_half or x == reversed_half // 10

    #USPS