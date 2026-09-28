import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Pair nums2 with nums1
        pairs = list(zip(nums2, nums1))

        # Sort by nums2 in descending order
        pairs.sort(reverse=True)

        heap = []
        nums1_sum = 0
        max_score = 0

        for num2, num1 in pairs:
            # Add nums1 value to the heap
            heapq.heappush(heap, num1)
            nums1_sum += num1

            # Keep only k largest nums1 values
            if len(heap) > k:
                removed = heapq.heappop(heap)
                nums1_sum -= removed

            # Once we have k elements, calculate score
            if len(heap) == k:
                score = nums1_sum * num2
                max_score = max(max_score, score)

        return max_score