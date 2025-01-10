s = ")"


def is_balanced(s):
    opp_dict = {')': '(', ']': '[', '}': '{'}

    def push(s, l):
        l.append(s)

    def pop(l):
        l.pop()

    l = []
    c = ""
    if len(s) > 1:
        for i in s:
            if i in opp_dict.values():
                push(i, l)
                c += i
            else:
                if len(l) > 0 and opp_dict[i] == l[-1]:
                    pop(l)
                    c += i
        if len(c) == len(s):
            return not l
        else:
            return False
    else:
        return False


print(is_balanced(s))
