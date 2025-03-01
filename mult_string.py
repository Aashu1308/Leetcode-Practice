class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def stoi(n: str) -> int:
            s = 0
            for i in range(len(n)):
                s += (ord(n[i]) - 48) * (10 ** (len(n) - i - 1))
            return s

        return str(stoi(num1) * stoi(num2))
