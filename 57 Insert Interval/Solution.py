# 57. Insert Interval
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            nstart, nend = newInterval[0], newInterval[1]
            start, end = intervals[i][0], intervals[i][1]

            if nend < start: 
                res.append(newInterval)
                return res + intervals[i:]
            
            elif nstart > end: 
                res.append(intervals[i])
            
            else:
                newInterval = [min(nstart, start), max(nend, end)]
        
        res.append(newInterval)

        return res 









        #         # edge case if we are at the beginning
        #         if i == 0:
        #             start, end = intervals[i][0], intervals[i][1]
        #             if nend < start: # no need to merge, just insert before 
        #                 intervals.insert(0, newInterval)
        #             else: # extend the first one left
        #                 intervals[i] = [nstart, end]
        #             return intervals
                

        #         # once we pass, then we insert before 
        #         left_start, left_end = intervals[i - 1][0], intervals[i - 1][1]
        #         right_start, right_end = intervals[i][0], intervals[i][1]

        #         expanded = False

        #         if nstart <= left_end: # merge with left, if necessary
        #             intervals[i - 1] = [left_start, nend]
        #             nstart = left_start
        #             expanded = True

        #         if nend >= right_start: # merge with right, if necessary
        #             intervals[i] = [nstart, right_end]
        #             nend = right_end
        #             expanded = True 

        #         if intervals[i][0] == intervals[i - 1][0]: # if we expanded the right to encapsulate the left, then remove the left
        #             intervals.pop(i)

        #         if not expanded: # need to insert the value
        #             intervals.insert(i, newInterval)

        #         return intervals 
        
        # intervals.append(newInterval)

        # return intervals

                



