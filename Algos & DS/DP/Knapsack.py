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
        return self.knapsack_recursive(weights, values, n-1, W)
      # Choose the maximum value obtained by either including or excluding the item
      include = values[i-1] + self.knapsack_recursive(n-1, W - weights[n-1])
      exclude = self.knapsack_recursive(n-1, W)
      return max(include, exclude)
    return helper(n, W)

class SolutionMemo:
  def knapsack_recursive(self, weights: List[int], values: List[int], W: int) -> int:
    n = len(weights)
    def helper(i: int, W: int) -> int:
      if i < 0 or W == 0:
        return 0
      
      # If weight of the ith item is more than the remaining capacity, skip it
      if weights[i] > W:
        return self.knapsack_recursive(i-1, W)
      
      # Choose the maximum value obtained by either including or excluding the item
      include = values[i] + helper(i-1, W - weights[i])
      exclude = helper(i-1, )
    
    

weights = [1,2,3]
values = [6,10,12]
W = 5
s = SolutionRec()
print(s.knapsack_recursive(weights, values, W))
