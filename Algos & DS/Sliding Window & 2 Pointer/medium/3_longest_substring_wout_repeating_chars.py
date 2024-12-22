'''
3. Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest 
substring without repeating characters.


1. Brute force: generate all substring and find longest with different characters
2. Optimized: Use a hashmap to shift left pointer to valid window 
'''

class SolutionBF:
  def lengthOfLongestSubstring(self, s: str) -> int:
    maxLen = 0
    
    for i in range(len(s)):
      seen = set()
      for j in range(i, len(s)):
        if s[j] in seen:
          break
        
        maxLen = max(maxLen, j-i+1)
        seen.add(s[j])
    return maxLen


class SolutionOP2:
  def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    l, maxLen = 0, 0

    for r in range(len(s)):
      while s[r] in seen:
        seen.remove(s[l])
        l += 1
        
      seen.add(s[r])
      maxLen = max(maxLen, r-l+1)
    return maxLen
        
class SolutionOP1:
  def lengthOfLongestSubstring(self, s: str) -> int:
    hm = {}
    l, r = 0, 0
    maxLen = 0
    
    for r in range(len(s)):
      if s[r] in hm:
        if hm[s[r]] >= l: # This range check is necessary. Ex: s = "abba" |  O: 3 | E: 2
          l = hm[s[r]] + 1 # Move l pointer to the stored/previously seen s[r] index + 1 to make window valid
      
      maxLen = max(maxLen, r-l+1)
      hm[s[r]] = r
    return maxLen
          

# s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
sol = SolutionBF()
print(sol.lengthOfLongestSubstring(s))