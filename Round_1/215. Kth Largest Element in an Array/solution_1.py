class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_k_max(nums, start, end, k):
            pvt_idx = self.partition(nums, start, end)

            if end - pvt_idx + 1 == k:
                return nums[pvt_idx]
            elif end - pvt_idx + 1 > k:
                return find_k_max(nums, pvt_idx + 1, end, k)
            else:
                return find_k_max(nums, start, pvt_idx - 1, k - (end - pvt_idx + 1))

        return find_k_max(nums, 0, len(nums) - 1, k)

    def partition(self, nums, start, end):
        pivot = nums[end]
        pvt_idx = start

        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            return

        for i in range(start, end):
            if nums[i] < pivot:
                swap(nums, i, pvt_idx)
                pvt_idx += 1

        swap(nums, pvt_idx, end)

        return pvt_idx