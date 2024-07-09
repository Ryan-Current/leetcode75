from typing import List

class Solution(object):
    def missingNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = (n * (n + 1)) / 2 # get whatever the total sum should be

        # subtract all numbers you see 
        for num in nums: 
            total = total - num 

        return total
