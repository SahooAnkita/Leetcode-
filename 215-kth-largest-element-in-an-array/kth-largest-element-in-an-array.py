import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            # Keep only k largest elements
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]