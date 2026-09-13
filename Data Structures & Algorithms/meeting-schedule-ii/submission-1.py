"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        sorted_start = sorted(interval.start for interval in intervals)
        sorted_end = sorted(interval.end for interval in intervals)
        max_counter = 0
        counter = 0
        i = 0
        j = 0
        while i < len(sorted_start) and j < len(sorted_end):
            if sorted_start[i] < sorted_end[j]:
                counter += 1
                i += 1
            elif sorted_end[j] <= sorted_start[i]:
                counter -= 1
                j += 1
            max_counter = max(counter, max_counter)
        return max_counter