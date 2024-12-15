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
class SolutionRec:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Helper function with memoization
        def dfs(i: int, prev: int, length: int, memo: dict) -> int:
            if i == len(s):
                return 0
            
            # If already computer for this char and len
            if (i, prev, length) in memo:
                return memo[(i, prev, length)]
            
            # Include current char if it continues the wraparound sequence
            if ord(p[i]) - ord(prev) == 1 or (prev == 'z' and p[i] == 'a'):
                length += 1
            else:
                length = 1
            
            # Store the max len of substring ending at p[i]
            max_lens[ord(s[i]) - ord('a')] = max(max_lens[ord(p[i]) - ord('a')], length)
            
            # Recursively check the next character
            res = dfs(i+1, p[i], length, memo)
            
            # Store in eemo and return the rsult
            memo[(i, prev, length)] = res
            return res
        
        # Array to store the max lens of substrings ending with each character
        max_lens = [0] * 26
        memo = {}
        
        # Start the recursive DFS
        dfs(0, '', memo)
        # Sum the max lens for all unique substrings
        return sum(max_lens)

class SolutionDP:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Array to store the max length of substrings ending with each character
        count = [0] * 26 # Current max len of consecutive substring
        maxLen = 0 # Current max len of consecutive substring
        
        for i in range(len(s)):
            # Check if the current character continues a valid substring
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                maxLen += 1
            else:
                maxLen = 1

            # Update count for p[i]
            idx = ord(s[i]) - ord('a')
            count[idx] = max(count[idx], maxLen)
    
        # Sum of all counts gives the number of unique substrings
        return sum(count)

s = "a"
# Output: 1
# Explanation: Only the substring "a" of s is in base.