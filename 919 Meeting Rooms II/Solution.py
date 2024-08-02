# 919 Meeting Rooms II
# Medium 

# Given an array of meeting time intervals consisting of start and end times, find the minimum number of conference rooms needed. 

# Example 

# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2
# Explanation:
# We need two meeting rooms for 
# room1: [0, 30]
# room2: [5, 10], [15, 20]

from typing import List 

class Interval:
    def __init__(self, start, end):
        self.start = start 
        self.end = end 


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        count = 0

        s = 0
        e = 0 

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else: 
                e += 1 
                count -= 1
            res = max(res, count)

        return res
    

intervals = [Interval(0, 30), Interval(0, 10), Interval(15, 30)]
print(Solution().minMeetingRooms(intervals))