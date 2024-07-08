from typing import List

class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop() 
            dfs(i+1, cur, total)    

        dfs(0, [], 0)
        return result
