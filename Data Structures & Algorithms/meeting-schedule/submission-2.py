"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda i: i.start)
        curr = intervals[0].end
        for i in range(1, len(intervals)):
            next_meeting = intervals[i].start
            if next_meeting < curr:
                return False
            else:
                curr = intervals[i].end
        
        return True