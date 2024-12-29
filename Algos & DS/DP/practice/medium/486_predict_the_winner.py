from typing import List

'''
Given an int array nums. 2 players: play 1 & player 2. They take turns.
Both start w/ score 0. At each turn the player takes a num from either end:
1. Start of the arr ie. nums[0]
2. End of arr ie nums[n-1]
* This reduces the len of the arr by 1
The player adds the chosen number to their score.
The game ends when there arr is empty

Return true if player 1 can win the game. 
If the scores are equal then player 1 is still the winner. Output true.
You may assume that both players are playing optimally.
'''

class SolutionMemo:
  def predictTheWinner(self, nums: List[int]) -> bool:
    n = len(nums)
    memo = [[None] * n for _ in range(n)]
    
    def dfs(left: int, right: int) -> bool:
      # Base case: only one pile left
      if left == right:
        return nums[left]
      
      # Check memoized result
      if memo[left][right] is not None:
        return memo[left][right]
      
      # Maximize the score difference
      pick_left = nums[left] - dfs(left + 1, right)
      pick_right = nums[right] - dfs(left, right - 1)
      memo[left][right] = max(pick_left, pick_right)
      return memo[left][right]
      
    # Start the recursion for the entire range
    return dfs(0, len(nums) - 1) >= 0

nums = [1,5,2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. 
# If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return false.

nums = [1,5,233,7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7.
# No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12),
# so you need to return True representing player1 can win.