#1 自己的解法 设计了一个开关
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        i = 0
        whether_star = False
        for char in s:
            stack.append(char)

        while stack:
            ch = stack.pop()
            if ch == ' ':
                if whether_star:
                    break
                else:
                    continue
            else:
                whether_star = True
                i += 1

        return i

#2 python写的
# s = "Hello"
# i = len(s)  # i = 5
# s[i]        # ❌ 报错：IndexError: string index out of range
#这就是为什么你看到的代码都从 len(s) - 1 开始向前扫描。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # 跳过末尾空格
        while i >= 0 and s[i] == ' ':
            i -= 1

        # 统计最后一个单词长度
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
