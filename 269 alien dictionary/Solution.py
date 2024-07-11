# 269. Alien Dictionary

# There is a new alient language that uses the english alphabet. However,
# the letters is unknown to you. 

# You are given a list of strings `words` from the alien language's dictionary, 
# where the strings in `words` are sorted lexicographically by the rules of 
# this new language. 

# Return a string of the unique letters in the new alient language sorted in 
# lexiocographically increasing order by the new language's rules. If there is
# no solution, return "". If there are multiple solutions, return any of them. 

# A string s is lexicographically smaller than a string `t` if at the first letter 
# where they differ, the letter in s comes before the letter in t in the alien 
# language. 

# Example 1: 
#     Input words = ["wrt", "wrf", "er","ett", "rtff"]
#     Output: "wertf"

from typing import List, Dict



    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        if len(words) == 0: 
            return ''

        if len(words) == 1:
            return words[0]
        
         
        graph: Dict[str, set[str]] = { c:set() for w in words for c in w}

        i = 0 
        # loop over all words, looking at 2 at a time
        while i < len(words) - 1: 
            current = words[i]
            next = words[i + 1]
    
            min_length = min(len(current), len(next))

            if len(current) > len(next) and current[:min_length] == next[:min_length]:
                return '' # if the prefix is the same, the longer word must be second

            # find the first letter where they differ and then make a node of which letter comes before
            for j in range(min_length):
                if current[j] != next[j]:
                    # letters differ here so make a node if one doesn't exist
                    graph[current[j]].add(next[j])
                    break
            i += 1
        
        visited: Dict[str, bool] = {} # False (visited) True (in current path)}
        reverse_order: List[str] = []
        # now we need to find the order of the graph, so search with a dfs
        def traverse(c: str):
            if c in visited: 
                return visited[c] # error here, should not visit a node in current path twice
            visited[c] = True # in current path
            
            for neighbor in graph[c]:
                if traverse(neighbor):
                    return True

            visited[c] = False # no longer in current path
            reverse_order.append(c)
        
        for c in graph: 
            if traverse(c): 
                return ""
        reverse_order.reverse()
        return "".join(reverse_order)


x = Solution()

words = ["wrt", "wrf", "er","ett", "rtff"]
# Expected output: "wertf"

print(x.alienOrder(words))
        

