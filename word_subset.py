word1 = ["amazon", "apple", "facebook", "google", "leetcode"]
word2 = ['l', 'e']

op = []


def word_count(s):
    a = [0] * 26
    for i in s:
        a[(ord(i) - ord('a'))] += 1
    return a


smax = [0] * 26
for s in word2:
    for i, c in enumerate(word_count(s)):
        smax[i] = max(smax[i], c)

for w in word1:
    a = word_count(w)
    flag = 0
    for i, j in zip(smax, a):
        if i > j:
            flag = 1
            break
    if not flag:
        op.append(w)
print(op)
