class SolutionRecursionK:
  def maxRepeating(self, sequence: str, word: str) -> int:
    def helper(k: int) -> int:
      # Base case: if word repeated k times is not a substring
      if word * k not in sequence:
        return k-1
      # Recursive case: check for k+1
      return rec(k+1)

    return rec(1)

class SolutionMemoHM:
  def maxRepeating(self, sequence: str, word: str) -> int:
    n, m = len(sequence), len(word)
    memo = {}

    # Helper function to check if `word` repeated `k` times is at sequence starting from index i
    def isRepeating(i, k):
      if (i, k) in memo:
        return memo[(i, k)]
      
      repeated_word = word * k
      if i + len(repeated_word) <= n and sequence[i:i + len(repeated_word)] == repeated_word:
        memo[(i, k)] = True
      else:
        memo[(i, k)] = False
      
      return memo[(i, k)]

    max_k = 0

    # Check for every starting index in the sequence
    for i in range(n):
      k = 1
      # Increase k until the word is not repeating
      while isRepeating(i, k):
        max_k = max(max_k, k)
        k += 1

    return max_k

class Solution:
  def maxRepeating(self, sequence: str, word: str) -> int:
    n, m = len(sequence), len(word)
    
    # DP array to store the max repeating counts ending at each index
    dp = [0] * n
    max_k = 0
    
    # Traverse through the sequence
    for i in range(m - 1, n):  # Start from index where word can fully fit
      # Check if the current substring matches the word
      if sequence[i - m + 1:i + 1] == word:
        if i - m >= 0:  # Check if there's a repeatable sequence before
          dp[i] = dp[i - m] + 1
        else:  # If no space before, just start a new repetition
          dp[i] = 1
        max_k = max(max_k, dp[i])

    return max_k