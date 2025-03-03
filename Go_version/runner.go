package main

import (
	"fmt"

	"aashu.com/leetcode/leetcode"
)

func main() {
	fmt.Println("Add digits of 38: ", leetcode.AddDigits(38))
	fmt.Println("Count absolute difference of 1 from [1,2,2,1]: ", leetcode.CountKDifference([]int{1, 2, 2, 1}, 1))
	fmt.Println("Count digit ones appearing upto 13: ", leetcode.CountDigitOne(13))
	fmt.Println("Applying operation over [1,2,2,1,1,0]: ", leetcode.ApplyOperations([]int{1, 2, 2, 1, 1, 0}))
	fmt.Println("Two sum for [2,7,11,15] with target 9: ", leetcode.TwoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println("Plus one for [1,9,9] is: ", leetcode.PlusOne([]int{1, 9, 9}))
	fmt.Println("Single non repeated number in [2,2,1] is: ", leetcode.SingleNumber([]int{2, 2, 1}))
	fmt.Println("Output of merging the two arrays [[1,2],[2,3],[4,5]] and [[1,4],[3,2],[4,1]] is: ", leetcode.MergeArrays([][]int{{1, 2}, {2, 3}, {4, 5}}, [][]int{{1, 4}, {3, 2}, {4, 1}}))
	fmt.Println("Result of sorting array [9,12,5,10,14,3,10] around pivot 10 is: ", leetcode.PivotArray([]int{9, 12, 5, 10, 14, 3, 10}, 10))
}
