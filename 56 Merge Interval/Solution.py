# 56. Merge Intervals
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the start value 
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        previous_end = output[0][1]

        for i in range(1, len(intervals)): 
            begin, end = intervals[i][0], intervals[i][1]

            if(begin <= previous_end):
                if end > previous_end:
                    output[len(output) - 1][1] = end
                    previous_end = end 
            else:
                output.append([begin, end])
                previous_end = end 


        return output