package leetcode

func PivotArray(nums []int, pivot int) []int {
	a := []int{}
	l1 := []int{}
	l2 := []int{}
	c := 0
	for i := range len(nums) {
		if nums[i] < pivot {
			l1 = append(l1, nums[i])
		} else if nums[i] > pivot {
			l2 = append(l2, nums[i])
		} else {
			c++
		}
	}
	a = append(a, l1...)
	pivotSlice := make([]int, c)
	for i := range pivotSlice {
		pivotSlice[i] = pivot
	}
	a = append(a, pivotSlice...)
	a = append(a, l2...)
	return a
}
