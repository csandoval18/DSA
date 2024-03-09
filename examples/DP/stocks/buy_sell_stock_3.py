from typing import List

def maxProfit(prices: List) -> int:
  n = len(prices)
  
  # Create a 3d dp table with dimensions (n) * n * 3 and
  # initialize it with -1 values
  dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
  
  def f(i: int, buy: int, cap: int) -> int:
    # Recursive function to calculate the max profit
    if i == n or cap == 0:
      return 0 # Base case: If we have reached the end of the arr or used up
      # all transactions, return zero profit
      
    if dp[i][buy][cap] != -1:
      return dp[i][buy][cap] # If the result is already computed, return it
    
    profit = 0
    if buy:
      # We can buy the stock
      profit = max(0 + f(i+1, 1, cap), prices[i] + f(i+1, 0, cap))
    else:
      