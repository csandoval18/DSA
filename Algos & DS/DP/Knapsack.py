from typing import List

'''
The Knapsack Problem is a classic optimization problem that can be solved in
various ways. I'll demonstrate three approaches here: a recursive solution, a
memoized (top-down dynamic programming) solution, and a bottom-up dynamic
programming solution.

Problem Statement:
Given a list of items with weights and values, and a maximum capacity W of a
knapsack, find the maximum value that can be obtained by selecting items such
that their total weight does not exceed W.

Each item can either be included or excluded, and there is only one instance of
each item (this is the 0/1 Knapsack problem
'''

# 1. Recursive Solution
class SolutionRec:
  def knapsack_recursive(self, weights: List[int], values: List[int], W: int) -> int:
    n = len(weights)
    def helper(n: int, W: int):
      # Base case: no items left or capacity is 0
      if n == 0 or W == 0:
        return 0
      
      # If weight of the nth item is more than the remaining capacity, skip it
      if weights[n-1] > W:
        return helper(weights, values, n-1, W)
      # Choose the maximum value obtained by either including or excluding the item
      include = values[n-1] + helper(n-1, W - weights[n-1])
      exclude = helper(n-1, W)
      return max(include, exclude)
    return helper(n, W)
  
  
class SolutionRec:
  def knapsack_recursive(self, weights: List[int], values: List[int], W: int) -> int:
    n = len(values)
    
    def helper(i: int, W: int):
      if i < 0 or W == 0:
        return 0
      
      if weights[i] > W:
        return self.helper(i-1, W)
      else:
        include = values[i] + helper(i-1, W - weights[i])
        exclude = helper(i-1, W)
        return max(include, exclude)
    return helper(n, W)


class SolutionMemo:
  def knapsack_recursive(self, weights: List[int], values: List[int], W: int) -> int:
    n = len(weights)
    memo = [[-1 for _ in range(W+1)] for _ in range(n)] 
    
    def helper(i: int, W: int) -> int:
      if i < 0 or W == 0:
        return 0
      
      # If weight of the ith item is more than the remaining capacity, skip it
      if weights[i] > W:
        return helper(i-1, W)
      # Choose the maximum value obtained by either including or excluding the item
      include = values[i] + helper(i-1, W - weights[i])
      exclude = helper(i-1, W)
      
      memo[i][W] = max(include, exclude)
      return memo[i][W]
    return helper(n-1, W)


class SolutionDP:
  def knapsack_recursive(self, weights: List[int], values: List[int], W: int) -> int:
    # Initialize DP table with 0s
    n = len(weights)
    dp = [[0 for _ in range(W+1)] for _ in range(n)]
    
    # Fill the first row (when considering only the first item)
    for w in range(W+1):
      if weights[0] <= w:
        dp[0][w] = values[0]
    
    # Fill dp table
    for i in range(n):
      for w in range(W+1):
        if weights[i] <= w:
          # Either include the item or exclude it
          dp[i][w] = max(values[i] + (dp[i-1][w-weights[i]]))
        else:
          # Exclude the item
          dp[i][w] = dp[i-1][w]
    # The max value for n items and capacity W
    return dp[n-1][w]

weights = [1,2,3]
values = [6,10,12]
W = 5
s = SolutionRec()
print(s.knapsack_recursive(weights, values, W))