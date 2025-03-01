package leetcode

func SingleNumber(nums []int) int {
	r := 0
	for _, i := range nums {
		r ^= i
	}
	return r
}
