# 295. Find Median from Data Stream
# Hard
# Topics
# Companies
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# min heap  
import heapq

class MedianFinder:

    def __init__(self):
        # 2 heaps, a minheap and a maxheap
        # they should be equal size with all elements of left less than right 
        # max of left and min of right give the middle of the list therefore
        self.leftheap = [] 
        self.rightheap = [] 
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftheap, -1 * num) # multiply by -1 to make this a max heap

        # all numbers in left must be <= right
        if self.leftheap and self.rightheap and (-1 * self.leftheap[0]) > self.rightheap[0]:
            # if we just pushed a number to left that should've been in right, move it to right
            val = -1 * heapq.heappop(self.leftheap)
            heapq.heappush(self.rightheap, val)

        # if the leftheap is bigger by more than 1, push to right
        if len(self.leftheap) > len(self.rightheap) + 1: 
            val = -1 * heapq.heappop(self.leftheap)
            heapq.heappush(self.rightheap, val)
            
        # if the rightheap is bigger by more than 1, push to left
        if len(self.leftheap) + 1 < len(self.rightheap): 
            val = heapq.heappop(self.rightheap)
            heapq.heappush(self.leftheap, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.leftheap) > len(self.rightheap):
            return self.leftheap[0] * -1 
        
        if len(self.leftheap) < len(self.rightheap):
            return self.rightheap[0] 

        return  (self.leftheap[0] * -1  + self.rightheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()