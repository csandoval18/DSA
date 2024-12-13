'''
LeetCode Problem 467. Unique Substrings in Wraparound String asks you to find
the number of unique substrings that are present in a string p, where all
substrings are also substrings of an "infinite wraparound string."

Problem Description:
The wraparound string s is defined as
"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz..." (infinitely repeated
lowercase alphabet). You need to determine how many unique substrings of p can
be found in this infinite wraparound string.

Key Observations:
1. The wraparound string implies a circular adjacency:
    - 'a' is adjacent to 'z', making the sequence wrap around
    - Example: "zab" is valid.
2. The consecutive characters condition:
    - A substring of p like "abc" or "xyzab" is valid if each character is
      alphabetically consecutive in the wraparound string.
3. Unique substrings:
    - Each substring can only contribute once, so we need to efficiently track
      and count unique valid substrings.

Approach:
To solve this problem:
1. Use dynamic programming to count the max length of valid substrings
   ending at each character.
2. Use an array count where count[char] represents the length of the longest
   valid substring ending with char.
3. The sum of all values in count gives the total number of unique  substrings. 
'''
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        base = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza"
        
        # Case 1:
        # len(s) == 1: answer = 1 | Since it is only one char
        
        
        
        

s = "a"
# Output: 1
# Explanation: Only the substring "a" of s is in base.