from typing import List

'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.
'''

'''
Approach:

1. Recursive backtracking:
  * Use a recursive function to explore numbers digit-by-digit, backtracking whenever a digit repeats.
  * Start with an initial set of unused digits from 0 to 9.
  * For each recursive call, choose an unused digit, add it to the current number, and continue.
  * If the currennt number reaches n digits (or less, if counting all numbers with fewer digits is allowed), count it as a valid number.
2. Base case:
  * When reaching n digits, stop further recursion.
3. Backtracking: 
  * After exploring one possibility with a chosen digit, remove it from the current combination and try the next available digit.
'''

# helper(pos, used):
# pos = The number of remaining position to fill.
# used = a list tracking whic digits are currently in use.
# When pos == 0, the recursion has generated a valid unique number, so it return 1

# Backtracking:
# For each digit from start to 9, if digit is unused (not used[digit]) mark it as used and recurse to the next position.
# After the recursive call, unmark digit to try other digits in its place (backtracking)

# TC: O(10^n) due to recursively exploring each possible digit
# SC: O(n) we use an array of size 10 for used digits and recursive digit

class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    # Base case: Only the number "0" is present so return count 1
    if n == 0:
      return 1  
      
    def helper(pos: int, used: List[bool]) -> int:
      # When pos == 0, we return 1, as we've formed a valid number
      if pos == 0:
        return 1
      
      cnt = 0
      # For the first digit (pos == n), don't allow "0" as the starting digit
      # This ensures that we do not have a leading zero in the second level of the recursive tree
      start = 1 if pos == n else 0
      for digit in range(start, 10):
        if not used[digit]: # Check if the digit is not already used
          used[digit] = True # Mark this digit as used 
          cnt += helper(pos - 1, used) # Recurse with reduced position
          used[digit] = False # Backtrack: unmark this digit
      return cnt
    
    # Sum up the counts for all possible lengths from 1 to n
    total_cnt = 1
    for length in range(1, n+1):
      used = [False] * 10
      total_cnt += helper(length, used)
    return total_cnt


class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
      return 1
      
    def helper(pos: int, ds: List[bool]) -> int:
      if pos == 0:
        return 1
      
      cnt = 0
      start = 1 if pos == n else 0
      for digit in range(start, 10):
        if not ds[digit]:
          ds[digit] = True
          cnt += helper(pos-1, ds)
          ds[digit] = False
      return cnt

    total_cnt = 1
    for length in range(1, n+1):
      ds = [False] * 10
      total_cnt += helper(length, ds)
    return total_cnt
      
      
class SolutionDP:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
      return 1 # Only the number "0" itself is valid when n = 0
    
    # Initialize dp array where dp[k] stores count of unique-digit numbers of length k
    dp = [0] * (n+1)
    # Base cases:
    dp[0] = 1 # dp[0] is 1 for the number 0
    dp[1] = 9 # There are 9 single-digit numbers (1 through 9)
    
    # Fill dp array for lengths 2 to n
    for length in range(2, n+1): 
      # Start with 9 single-digit numbers (1 through 9)
      cnt = 9
      # Multiply choices for each subsequent position
      # formula 10 - length + 1 
      for i in range(9, 10 - length, -1): # Inner loop decreases the number of digits available to pick on each position
        count *= i
      dp[length] = count
      
    total_cnt = sum(dp)
    return total_cnt
          
          
class SolutionSO:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
      return 1
    
    total_cnt = 1
    curr_cnt = 9
    
    for length in range(1, n+1):
      if length == 1:
        total_cnt += curr_cnt
      else:
        curr_cnt *= 10 - length + 1
        total_cnt += curr_cnt
    return total_cnt
      

n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

#        Start
#     /    |    |    \     ...      \
#    1     2    3     4              9
#   / \   / \  / \   / \            / \
#  0   2 0   1 0   1 0   1   ...   0   8
#      |     |     |     |          |
#      3     3     4     4          9
#     ...   ...   ...   ...        ...
