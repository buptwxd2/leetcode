# use heap algorithm

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap = []  # min heap with size k
        for num in nums[:k]:
            heapq.heappush(heap, num)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

"""
Results:
Runtime: 64 ms, faster than 78.65% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.6 MB, less than 10.00% of Python3 online submissions for Kth Largest Element in an Array.
"""