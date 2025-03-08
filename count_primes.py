class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [1] * (n)
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for m in range(i * i, n, i):
                    primes[m] = 0
        print(primes)
        return sum(primes)


s = Solution()
print(f"op is :{s.countPrimes(6)}")
