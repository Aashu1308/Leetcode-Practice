def appendAndDelete(s, t, k):
    clen = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            clen += 1
        else:
            break
    stepcount = (len(s) - clen) + (len(t) - clen)
    if stepcount == k or k >= (len(s) + len(t)):
        print("yes", stepcount)
    else:
        print("No", stepcount)


print(appendAndDelete("hackerhappy", "hackerrank", 9))
print(appendAndDelete("aba", "aba", 7))
print(appendAndDelete("yu", "y", 2))
print(appendAndDelete("abcd", "abcdert", 10))
print(appendAndDelete("abcd", "fda", 15))
