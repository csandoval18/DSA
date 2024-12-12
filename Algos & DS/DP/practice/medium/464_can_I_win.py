'''
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. 
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from
1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player
to move can force a win, otherwise, return false. Assume both players play optimally.
'''

# Approach:
# The problem can be solved using backtracking with memoization. Key considerations:

# 1. Constraints and Observations:
#   - If the sum of all numbers (from 1 to maxChoosableInteger) is less than desiredTotal, it's impossible for either player to win.
#   - If maxChoosableInteger ≥ desiredTotal, the first player can simply choose desiredTotal directly and win.

# 2. State Representation:
#   - Use a bitmask (usedNumbers) to represent which numbers are already picked.
#   - Use a recursive function to explore all possible moves.

# 3. Memoization:
#   - Memoize results based on the current usedNumbers and remainingTotal to avoid redundant calculations.

# 4. Base Case:
#   - If the remainingTotal ≤ 0, the current player loses.

class Solution:
  def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
      return False
    if maxChoosableInteger >= desiredTotal:
      return True

    memo = {}

    def can_win(used_numbers: int, remaining_total: int) -> bool:
      if remaining_total <= 0:
        return False
      if used_numbers in memo:
        return memo[used_numbers]
      
      for i in range(maxChoosableInteger):
        current_mask = 1 << i
        if not (used_numbers & current_mask):  # If the number i+1 is not used
          # Choose the number i+1 and toggle its bit
          if not can_win(used_numbers | current_mask, remaining_total - (i + 1)):
            memo[used_numbers] = True
            return True
      
      memo[used_numbers] = False
      return False

    return can_win(0, desiredTotal)


class Solution:
  def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    if desiredTotal <= 0:
      return True
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
      return False
      
    dp = [-1] * (1 << maxChoosableInteger)
    
    def dfs(state, remaining):
      if remaining <= 0:
        return False
      if dp[state] != -1:
        return dp[state] == 1
      for i in range(maxChoosableInteger):
        if (state & (1 << i)) == 0:
          if not dfs(state | (1 << i), remaining - (i + 1)):
            dp[state] = 1
            return True
      dp[state] = 0
      return False
    return dfs(0, desiredTotal)

maxChoosableInteger = 10
desiredTotal = 11
# Output: False

maxChoosableInteger = 10
desiredTotal = 0
# Output: True

maxChoosableInteger = 10
desiredTotal = 1
# Output: True