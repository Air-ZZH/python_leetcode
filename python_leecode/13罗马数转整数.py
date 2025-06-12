class Solution:

    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        sh = reversed(s)

        # 从右往左遍历字符串
        for ch in sh:
            value = roman_map[ch]
            if value < prev_value:
                total -= value  # 小的在右边大的前面，要减
            else:
                total += value  # 否则加
            prev_value = value

        return total

# 85 --> LXXXV
# 95 --> XCV