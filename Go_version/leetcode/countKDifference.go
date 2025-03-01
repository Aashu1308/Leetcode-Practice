package leetcode

func CountKDifference(nums []int, k int) int {
	d := make(map[int]int)
	c := 0
	for i := range nums {
		j := nums[i]
		if count, ok := d[j+k]; ok {
			c += count
		}
		if count, ok := d[j-k]; ok {
			c += count
		}
		d[j]++
	}
	return c
}
