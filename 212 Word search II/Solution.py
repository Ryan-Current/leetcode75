# 212. Word Search II
# Hard
# Topics
# Companies
# Hint
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

from typing import List, Set, Optional

# set's dont work the way I want them to in python
# class TrieNode: 
#     def __init__(self, letter: str = '', word_end: bool = False, next_letters: Set['TrieNode'] = {}):
#         self.letter: str = letter
#         self.word_end: bool = word_end 
#         self.next_letters: Set['TrieNode'] = next_letters
    
#     def __hash__(self): 
#         return hash(self.letter)
    
#     def __eq__(self, value: object) -> bool:
#         if not isinstance(value, TrieNode):
#             return False 
#         return self.letter == value.letter
    
#     def insert(self, node: 'TrieNode', isWordEnd: bool) -> 'TrieNode':
#         if node not in self.next_letters:
#             self.next_letters.add(node)
        
#         if not self.next_letters[node].word_end:
#             self.next_letters[node].word_end = isWordEnd

#         return self.next_letters[node]
    
#     def next(self, letter: str) -> Optional['TrieNode']:
#         return self.next_letters[TrieNode(letter)]
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = dict()

        for word in words: 
            current = trie_root
            for letter in word: 
                current = current.setdefault(letter, {})
            current['end'] = None

        print(trie_root)

        found: Set[str] = set()

        def canvisit(i, j, visited):
            return 0 <= i and i < len(board) and 0 <= j and j < len(board[i]) and (i, j) not in visited

        def search_words(trie, word, visited : Set, i, j):
            letter = board[i][j]

            if letter not in trie: 
                return
            
            word = word + letter
            visited = visited.copy()
            visited.add((i, j))

            if 'end' in trie[letter]:
                found.add(word)
            
            # left
            if canvisit(i - 1, j, visited):
                search_words(trie[letter], word, visited, i - 1, j)
            # down
            if canvisit(i, j - 1, visited):
                search_words(trie[letter], word, visited, i, j - 1)
            # right
            if canvisit(i + 1, j, visited):
                search_words(trie[letter], word, visited, i + 1, j)
            # up
            if canvisit(i, j + 1, visited):
                search_words(trie[letter], word, visited, i, j + 1)

            

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                search_words(trie_root, '', set(), i, j)

        return list(found)
    


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# board = [["a"]]
# words = ["a"]

x = Solution()

print(x.findWords(board, words))