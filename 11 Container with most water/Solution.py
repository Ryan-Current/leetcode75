from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        def area(left, right):
            x = right - left
            y = height[left] if height[left] < height[right] else height[right]
            return x * y
        
        # init left and right to the edges to maximize width for area 
        left = 0 
        right = len(height) - 1

        max = 0 

        # move them closer, always taking the smaller one and moving it
        while left < right: 
            a = area(left, right)

            if max < a: 
                max = a 

            if height[left] < height[right]:
                left += 1 
            else: 
                right -= 1
        
        return max 

        

