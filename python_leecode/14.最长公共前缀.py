#法1 法2 都是python写的 还没看

#法1 手动实现 s.startswith(prefix) 的效果
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            # 用你手写的 starts_with 代替 startswith
            while not self.starts_with(s, prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

    def starts_with(self, s: str, prefix: str) -> bool:
        if len(prefix) > len(s):
            return False

        for i in range(len(prefix)):
            if s[i] != prefix[i]:
                return False
        return True

# 法二 用 while 和下标来实现字符串缩短