class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(set(pattern)) == len(set(s.split())) == len(
            set(zip(pattern, s.split()))
        ) and len(pattern) == len(s.split())
