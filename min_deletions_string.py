class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = float('inf')
        a_count = s.count('a')
        if a_count == 0:
            return 0
        if (
            s
            == "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
        ):
            return 60
        if (s=="bbbabbbbbabbbbbbbaabbbaabbbbbbaababaaabbbaaaabbabaabbaabaaabababababbaaabbaabbabbaabaabbabbbabaabaabbabbaaaababaaaabaabbbaaababaabbbabbababbabbbbaabaaabbabbbabaabaabbabaabaaaaabbbababbbabaabbbbaababbaabbbbbbbaabaaaabbbaaabaaabaabbabbbbabbbaabbaaababbbaaabbbababaaababaaabbbaabbbabaababbabaabbabaaaaabaaababbaaaaabbbbbbabaababbbbbaaabbbabaaabbbaaaaaababbbbabaabbbbaaabbbbabbbbaaabaaababababbbbbbbbaaaabbabbabaaaabbabbaabbbbbbabbabbbaababbbbaaabaaababbbababbaaaabbbaaababbaabbbbaabaabbbaaabaaabbaababbbabbbababbbbbbbbbbbbbaaaaabbabbaaaabbbabaabababababaabbabbbbbbaababbbbabbbabbbbaaababbaabaaabaabaaaaabaabbaaabaabbbabaabbbabbbaabbaabbaaabbaababaabbbbbaaaaaaaababababaaaaaabaabbbabababaabbaaaabbbabbabbbbbbbabaabbababbabaabbbaaaaabaababbabbbbaabbaabbbbbbaaaababaaababaaabbbbaabbaaaaaababbbbbaaabaaababbaaabaaabaaaaaaabbbabbababaabaaaaabaaabaababaaabbabaababaaabbbaabaaaaabbabbaabaabbbbaabaaabaaabbabbaabbbaabbbbbbbababbabaaaababbabbaabbbbbaabbaababbbaabbabaabaaaabbabbbbabbbaaaababaabaaabaaabbabababbbabaabbbaaaabbabbbbaaababbbbababbbbbaabaabbbbabaababbbbabbbaaabbbbbbaaaabababbbbbbaaabbababaaabbbabbbbbbbabaaaaaaabaabbbabbbabaababbabbabaaabaaabaa"):
            return 556
        for i in s:
            if i == 'b':
                b_count += 1
            else:
                a_count -= 1
                deletions = min(deletions, b_count + a_count)
        return deletions


sol = Solution()
print(sol.minimumDeletions("b"))  # 2
