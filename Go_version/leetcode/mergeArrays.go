package leetcode

func MergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	a := [][]int{}
	i := 0
	j := 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i][0] < nums2[j][0] {
			a = append(a, nums1[i])
			i++
		} else if nums2[j][0] < nums1[i][0] {
			a = append(a, nums2[j])
			j++
		} else {
			a = append(a, []int{nums1[i][0], nums1[i][1] + nums2[j][1]})
			i++
			j++
		}
	}
	if i < len(nums1) {
		for i < len(nums1) {
			a = append(a, nums1[i])
			i++
		}
	} else if j < len(nums2) {
		for j < len(nums2) {
			a = append(a, nums2[j])
			j++
		}
	}
	return a
}
