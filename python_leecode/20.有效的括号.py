class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        HashMap = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in HashMap:
                stack.append(char)

            elif char in HashMap.values():
                if not stack or HashMap[stack.pop()] != char:
                    return False

        return not stack

'''' 遍历字符串 s，时间复杂度：O(n)
stack.pop()
print(stack)


s = 'abcdefg'
stack2 = []
print(type(stack2))
for char in s:
    x = char
    stack2.append(x)


print(stack2)
# 遍历字符串，
#压入栈的先进来的是) ] }
# 开口朝右边的 先检查是否stack空了 --> fales
# 然后pop一个出来看是否跟 开口右边的配对 如果不是 F
# 遍历完所有元素以后，stack空了，则T，else F

stack = []
HashMap = {'(': ')', '[':']', '{': '}'}
if '}' in HashMap:
    print(1)
else:print(0)

'''