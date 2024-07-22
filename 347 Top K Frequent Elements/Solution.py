# 347. Top K Frequent Elements
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums: 
            dict.setdefault(num, 0)
            dict[num] += 1

        counts = [[] for i in range(len(nums) + 1)]

        for num, cnt in dict.items(): 
            counts[cnt].append(num)

        res = []

        for i in range(len(counts) - 1, 0, -1):
            for n in counts[i]: 
                res.append(n)
                if len(res) == k:
                    return res

