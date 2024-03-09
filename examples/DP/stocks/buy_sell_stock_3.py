from typing import List

def maxProfit(prices: List) -> int:
  n = len(prices)
  
  # Create a 3d dp table with dimensions (n) * n * 3 and
  # initialize it with -1 values
  dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]