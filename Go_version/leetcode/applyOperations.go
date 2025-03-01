package leetcode

func ApplyOperations(nums []int) []int {
	for i := range len(nums) - 1 {
		if nums[i] == nums[i+1] {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}
	j := 0
	for i := range len(nums) {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
	}
	for j < len(nums) {
		nums[j] = 0
		j++
	}
	return nums
}
