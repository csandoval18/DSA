# 1155. Number of Dice Rolls With Target Sum

# You have n dice & each die has k faces numbered from 1 to k

# Given 3 ints n, k, target
# Return the num of possible ways (out of the k^n total ways) to roll
# to roll the dice, so the sum of the face-up numbers = target.

# Since the answer may be too large, return it modulo 10^9 + 7

def numRollsToTarget(n: int, k: int, target: int) -> int:
  MOD = 10**9+7
  
  # dp[i][j]: Number of ways to get sum j using i dice
  dp = [[0] * (target+1) for _ in range(n+1)]
  
  # Initialize base case: one way to get sum 0 using 0 dice
  dp[0][0] = 1
  
  for i in range(1, n+1):
    for j in range(1, target+1):
      # Iterate over possible outcomes of the current die
      for k in range(1, min(j, k)+1):
        dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD
  return dp[n][target]
  
  