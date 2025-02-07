class Solution:
    def reverseParentheses(self, s: str) -> str:
        l = []
        ss = ""
        for i in s:
            # print("current char:",i,"open count:",oc)
            if i == '(':
                l.append(ss)
                ss = ""
            elif i == ')':
                ss = l.pop() + ss[::-1]
            else:
                ss += i
            # print(l)
        return ss
