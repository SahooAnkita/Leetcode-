import heapq

class SmallestInfiniteSet:

    def __init__(self):
        # Smallest number that has never been popped
        self.current = 1

        # Numbers that were added back
        self.heap = []

        # Prevent duplicate numbers in the heap
        self.added = set()

    def popSmallest(self) -> int:
        # If we have numbers that were added back,
        # the smallest one should be returned first.
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num

        # Otherwise return the next number from the infinite set.
        num = self.current
        self.current += 1
        return num

    def addBack(self, num: int) -> None:
        # Only numbers that have already been popped
        # can actually be added back.
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)