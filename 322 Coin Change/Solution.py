# 322. Coin Change
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from typing import List 


# DFS approach


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         if(amount == 0):
#             return 0

#         if(amount < 0):
#             return float('-inf')

#         arr = []
#         for c in coins:
#             numNeeded = self.coinChange(coins, amount - c)
#             if(numNeeded >= 0 ):
#                 arr.append(1 + numNeeded)

#         return min(arr)
        
# coins = [1, 2, 5]
# amount = 11 
# # answer is 3

# print(Solution().coinChange(coins, amount))

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float('inf')] * (amount + 1)
        cache[0] = 0

        for a in range(1, amount + 1):
            for c in coins: 
                if a - c >= 0: 
                    cache[a] = min(cache[a], 1 + cache[a - c])

        return cache[amount] if cache[amount] != float('inf') else -1
    
coins = [1, 2, 5]
amount = 11 
# answer is 3

print(Solution().coinChange(coins, amount))