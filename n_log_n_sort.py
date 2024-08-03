class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr: list[int], left: int, mid: int, right: int):
            n1 = mid - left + 1
            n2 = right - mid
            larr = [arr[left + i] for i in range(n1)]
            rarr = [arr[mid + 1 + j] for j in range(n2)]
            i = 0
            j = 0
            k = left
            while i < n1 and j < n2:
                if larr[i] <= rarr[j]:
                    arr[k] = larr[i]
                    i += 1
                else:
                    arr[k] = rarr[j]
                    j += 1
                k += 1
            while i < n1:
                arr[k] = larr[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = rarr[j]
                j += 1
                k += 1

        def sort(arr: list[int], left: int, right: int):
            if left >= right:
                return
            mid = left + (right - left) // 2
            sort(arr, left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

        sort(nums, 0, len(nums) - 1)
        return nums


sol = Solution()
print(sol.sortArray([5, 1, 1, 2, 0, 0]))
