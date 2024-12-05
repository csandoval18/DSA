'''
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. 
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from
1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player
to move can force a win, otherwise, return false. Assume both players play optimally.
'''

# Solution

# 1. Key obeserbations:
#   * If the total sum of all integers in range(1, maxChoosableInteger) < than desiredTotal, neither player can win.
#   * The game state can be represented using a bitmask, where each bit indicates whether a number is available for selection.
# 2. Recursive Function:
#   * Base Case: If the current player can pick a number to reach or exceed desiredTotal, they win.
#   * Recursive Case: For each available number, simulate picking it and let the opponent play. If the opponent cannot win in the next step, the current player wins.
# 3. Memoization
#   * Store results for already computed states to avoid redundant calculations.

class SolutionRec:
  def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
    # If the sum of all numbers is less than the desired total, it's impossible to win
      return False
    
    def helper(rem, used_nums):
      for i in range(1, maxChoosableInteger + 1): # Try every number from 1 to maxChoosableInteger
        curr_bit = 1 << i # Bitmask for current number
        
        if used_nums & curr_bit == 0:  # If the number is not used
          if rem - i <= 0 or not helper(rem - i, used_nums | curr_bit): # If picking this number wins the game, or the opponent loses
            return True
      
      # If no winning move is found
      return False
    return helper(desiredTotal, 0)


class SolutionMemo:
  def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    # If the sum of all numbers is less than the desired total, it's impossible to win
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
      return False
    
    memo = {}
    
    def helper(rem, used_nums):
      # Check if we have already computed this state
      if used_nums in memo:
        return memo[used_nums]
      
      for i in range(1, maxChoosableInteger + 1): # Try every number from 1 to maxChoosableInteger
        curr_bit = 1 << i # Bitmask for current number
        
        if used_nums & curr_bit == 0:  # If the number is not used
          if rem - i <= 0 or not helper(rem - i, used_nums | curr_bit): # If picking this number wins the game, or the opponent loses
            memo[used_nums] = True
            return True
      
      # If no winning move is found
      memo[used_nums] = False
      return False
    return helper(desiredTotal, 0)


def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
  # If the sum of all numbers is less than the desired total, it's impossible to win
  if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
    return False

  # Memoization list to store the results of states
  memo = [-1] * (1 << maxChoosableInteger)  # Initialize with -1 (uncomputed states)

  def helper(rem: int, used_nums: int) -> bool:
    # Check if we have already computed this state
    if memo[used_nums] != -1:
      return memo[used_nums] == 1

    for i in range(1, maxChoosableInteger + 1): # Try every number from 1 to maxChoosableInteger
      curr_bit = 1 << i # Bitmask for current number
      
      if used_nums & curr_bit == 0:  # If the number is not used
        if rem - i <= 0 or not helper(rem - i, used_nums | curr_bit): # If picking this number wins the game, or the opponent loses
          memo[used_nums] = True
          return True
    
    # If no winning move is found
    memo[used_nums] = False
    return False
  return helper(desiredTotal, 0)


maxChoosableInteger = 10
desiredTotal = 11
# Output: False

maxChoosableInteger = 10
desiredTotal = 0
# Output: True

maxChoosableInteger = 10
desiredTotal = 1
# Output: True