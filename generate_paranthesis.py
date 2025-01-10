n = 3
l = []


def gen(n):
    def backtrack(oc, cc, comb):
        if len(comb) == 2 * n:
            l.append("".join(comb))
            return
        if oc < n:
            comb.append("(")
            backtrack(oc + 1, cc, comb)
            comb.pop()
        if cc < oc:
            comb.append(")")
            backtrack(oc, cc + 1, comb)
            comb.pop()

    backtrack(0, 0, [])
    return l


print(gen(n))
