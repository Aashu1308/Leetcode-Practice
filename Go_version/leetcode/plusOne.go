package leetcode

func PlusOne(digits []int) []int {
	x := len(digits) - 1
	if digits[x] != 9 {
		digits[x]++
		return digits
	} else {
		if len(digits) == 1 {
			return []int{1, 0}
		} else {
			for x >= 0 && digits[x] == 9 {
				digits[x] = 0
				x--
			}
			if x < 0 {
				result := []int{1}
				result = append(result, digits...)
				return result
			} else {
				digits[x]++
			}
		}

	}
	return digits
}
