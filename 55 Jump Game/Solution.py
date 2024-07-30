# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1): 
            if nums[i] + i >= goal: # if our range can pass the goal, then move it 
                goal = i

        return goal == 00


        # # move backwards, marking each location if it can reach or not
        # nums[len(nums) - 1] = 1 # mark the last location as you can get there
        # for i in range(len(nums) - 2, -1, -1): 
        #     maxJump = nums[i]

        #     # if you can reach any at the current position then you can reach the end 
        #     if any(i == 1 for i in nums[i + 1:i + maxJump + 1]): 
        #         nums[i] = 1
        #     else:
        #         nums[i] = 0 

        # return nums[0] 
    
        # # optimization, instead of checking if you can reach any of the numbers with your jump, you can just take the earliest one since it will be hit first
                





