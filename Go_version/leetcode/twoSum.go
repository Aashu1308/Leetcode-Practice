package leetcode

func TwoSum(nums []int, target int) []int {
	d := make(map[int]int)
	for i, num := range nums {
		comp := target - nums[i]
		if idx, ok := d[comp]; ok {
			return []int{idx, i}
		}
		d[num] = i
	}
	return []int{}
}
