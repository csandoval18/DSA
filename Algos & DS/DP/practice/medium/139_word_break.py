from typing import List


class SolutionRecSplicing:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # Base case: if the string is empty, we can segment it successfully
    if not s:
      return True
    
    # Try every possible prefix of s
    for i in range(1, len(s) + 1):
      # Check if the prefix s[0:i] is a valid word
      if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
        return True
    
    return False


class SolutionRecIndexes:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict) # Convert worddict to a set for faster lookups
    n = len(s)
    
    def helper(start: int):
      # Base case: if start reaches the end of the string, we've successfully segmented it
      if start == n:
        return True
      
      # Try every possible end index from start+1 to n
      for end in range(start+1, n+1):
        # Check if the substring s[start:end] is in the dictionary and check remaining substring through recursion
        if s[start:end] in word_set and helper(end): # helper(end) recurses and sets the end of the current substring as the start of the new substring to check
          return True
      
      # If no valid segmentation is found, return False
      return False
    return helper(0)
    
    
class SolutionMemo:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * n # Initialize a list to store results for each starting index
    
    def helper(start: int):
      if start == n:
        return True
      
      if dp[start] != -1:
        return dp[start]
      
      for end in range(start+1, n+1):
        if s[start:end] in word_set and helper(end):
          dp[start] = True
          return True
      return False
    return helper(0)


class SolutionDP:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    
    for start in range(1, n+1):
      if not dp[start]:
        continue
      
      for end in range(start+1, n+1):
        if s[start:end] in word_set:
          dp[end] = True
    return dp[n]
    
s = "leetcode"
wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code"

# s = "applepenapple"
# wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# Output: false