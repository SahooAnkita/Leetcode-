import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)

        # If both candidate ranges overlap,
        # all workers are candidates.
        if 2 * candidates >= n:
            return sum(heapq.nsmallest(k, costs))

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Fill left heap
        for _ in range(candidates):
            heapq.heappush(left_heap, costs[left])
            left += 1

        # Fill right heap
        for _ in range(candidates):
            heapq.heappush(right_heap, costs[right])
            right -= 1

        total_cost = 0

        for _ in range(k):

            # Choose from left if:
            # - left cost is smaller
            # - costs are equal
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    total_cost += heapq.heappop(left_heap)

                    # Add next worker from left
                    if left <= right:
                        heapq.heappush(left_heap, costs[left])
                        left += 1

                else:
                    total_cost += heapq.heappop(right_heap)

                    # Add next worker from right
                    if left <= right:
                        heapq.heappush(right_heap, costs[right])
                        right -= 1

            elif left_heap:
                total_cost += heapq.heappop(left_heap)

            else:
                total_cost += heapq.heappop(right_heap)

        return total_cost