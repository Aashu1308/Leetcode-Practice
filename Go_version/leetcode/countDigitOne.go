package leetcode

func CountDigitOne(n int) int {
	c := 0
	i := 1
	for i <= n {
		d := i * 10
		c += (n / d) * i
		if (n % d) >= (i * 2) {
			c += i
		} else if (n % d) >= (i) {
			c += (n % d) - i + 1
		}
		i *= 10
	}
	return c
}
