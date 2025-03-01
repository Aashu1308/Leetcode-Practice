package leetcode

import (
	"strconv"
)

func AddDigits(num int) int {
	if num < 10 {
		return num
	}
	s := 0
	st := strconv.Itoa(num)
	for i := range st {
		s += int(st[i] - '0')
	}
	if s < 10 {
		return s
	}
	return AddDigits(s)
}
