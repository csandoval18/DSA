from typing import List


class SolutionRecursion:
  def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    def helper(i: int, prev_group: int) -> int:
      if i == len(words):
        return 0
      
      # Case 1: Include the curr word if its group is different from the previous group's
      include = 0
      if groups[i] != prev_group:
        include = 1 + helper(i+1, groups[i])
      
      # Case 2: Skip the current word
      skip = helper(i+1, prev_group)
      
      # Return the max of the two cases
      return max(include, skip)
    return helper(0, -1) 
    
class SolutionTabulation:
  def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    return

class SolutionSO:
  def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    if not words or not groups:
      return []
    
    res = [words[0]]
    prev_group = groups[0]

    for i in range(1, len(words)):
      if groups[i] != prev_group:
        res.append(words[i])
        prev_group = groups[i]
    return res

words = ["e","a","b"]
groups = [0,0,1]

# "e" belongs to group 0
# "a" belongs to group 0
# "b" belongs to group 1
# "e" and "a" are adjacent
# Output: ["e","b"]

# Recursive Thought Process

# - Task: Find the longest subsequence of words where no two consecutive words belong to the same group.
# 1. For each word at index i, we have two choices:
#   * Include the word in our subsequence if its group is different from the previous word's group.
#   * Skip the word an d try to find the solution for the remaining words.
# 2. The base case is when we have only one word left, which can always be included in the subsequence.

# Recursive Function
# Let’s define a recursive function findLongest(i, prev_group):

# * i is the current index of the word we are considering.
# * prev_group is the group of the last word we included in the subsequence.
# * The function will return the length of the longest valid subsequence starting from the i-th word, given that the previous word belongs to prev_group.

# Recursive Formula:
# Case 1: Include the current word words[i] if groups[i] != prev_group:
#   In this case, the answer is 1 + findLongest(i + 1, groups[i]).
# Case 2: Skip the current word:
#   The answer is findLongest(i + 1, prev_group).

# The overall result will be the maximum of these two cases:
# findLongest(i, prev_group) = max(
#     1 + findLongest(i + 1, groups[i]) if groups[i] != prev_group else 0,
#     findLongest(i + 1, prev_group)
# )