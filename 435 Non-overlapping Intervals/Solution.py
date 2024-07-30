# 435. Non-overlapping Intervals
# Medium
# Topics
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104


from typing import List 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        res = 0

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd: # overlapping, and we want to remove the one that ends later
                res += 1
                prevEnd = min(prevEnd, end) # take the one that ended first, to minimize the chance of an overlap with the next
            else: 
                prevEnd = end

        return res 