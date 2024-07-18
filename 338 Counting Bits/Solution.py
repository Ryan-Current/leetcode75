# 338. Counting Bits
# Easy
# Topics
# Companies
# Hint
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


# 0  - 0000|
# 1  - 0001|  *
# 2  - 001|0  
# 3  - 001|1
# 4  - 01|00  *
# 5  - 01|01
# 6  - 01|10
# 7  - 01|11
# 8  - 1|000  *
# 9  - 1|001
# 10 - 1|010
# 11 - 1|011
# 12 - 1|100
# 13 - 1|101
# 14 - 1|110
# 15 - 1|111

# 0 is 0, 1 is 1 
# left if new significant bit (1 + {old work})
# right is repeated from before (old work), accessed with n - power of 2 that is below, so 2 for 2 and 3, 4 for 4-7, 8 for 8-15, etc.

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]

        cur_power = 0

        for i in range(1, n + 1): 
            if i == 2 ** (cur_power + 1): 
                cur_power += 1
            offset = 2 ** cur_power
            arr.append(1 + arr[i - offset])

        return arr 
    
print(Solution().countBits(2))