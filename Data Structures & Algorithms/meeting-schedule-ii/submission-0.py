"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_meetings = 0 
        end_times = []
        start_times = []
        for i in range (0, len(intervals)):
            end_times.append(intervals[i].end)
            start_times.append(intervals[i].start)
            
        end_times.sort()
        start_times.sort()

        e,s = 0,0
        highest = 0
        for i in range (0,len(intervals)):
            if start_times[s] < end_times[e]:
                max_meetings = max_meetings + 1
                s += 1
            elif start_times[s] >= end_times[e]:
                max_meetings = max_meetings - 1
                e += 1
        
            if highest < max_meetings:
                highest = max_meetings
            else:
                continue

        return highest
        



