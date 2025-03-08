package leetcode

func CheckPowersOfThree(n int) bool {
	pow := 1
	for pow < n {
		pow *= 3
	}
	for n > 0 {
		if n >= pow {
			n -= pow
		}
		if n >= pow {
			return false
		}
		pow /= 3
	}
	return true
}
