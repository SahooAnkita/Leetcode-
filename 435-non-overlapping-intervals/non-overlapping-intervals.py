class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removals = 0
        previous_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < previous_end:
                removals += 1
            else:
                previous_end = end

        return removals