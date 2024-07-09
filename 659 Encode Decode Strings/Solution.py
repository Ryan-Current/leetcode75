# 659 · Encode and Decode Strings
# Algorithms
# Medium
# Accepted Rate
# 64%

# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

# WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


# Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

# Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

from typing import List

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs : List[str]) -> str:
        return ''.join([f'{len(s)}:{s}' for s in strs])


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:
        strs = []
        while str != '':
            i = str.index(':')

            num_chars = int(str[0:i])
            strs.append(str[i + 1: num_chars + i + 1])
            str = str[num_chars + i + 1:]

        return strs
    

l = ["hello", ":how", "are4:you"]

print(Solution().decode(Solution().encode(l)))