from typing import List

def maxProfitMemo(prices: List[int]) -> int:
  def f(i: int, buy: int, dp) -> int:
    # Base case when prices is exahusted, we can no longer get any profit
    if i == n:
      return 0
      
    if dp[i][buy] != -1:
      return dp[i][buy]
    
    profit = 0
    if buy:
      profit = max(-prices[i] + f(i+1, 0, dp), # Take
      0 + f(i+1, 1, dp)) # Not take
    else:
      profit = max(prices[i] + f(i+1, 1, dp), 0 + f(i+1, 0, dp))
    
    return profit
  
  n = len(prices)
  dp = [[-1]*2 for _ in range(n+1)]
  return f(0, 1, dp)


def maxProfitTab(prices: List[int]) -> int:
  n = len(prices)
  dp = [[0]*2 for _ in range(n+1)]
  dp = [n][0] = dp[n][1] = 0
  
prices = [7,1,5,3,6,4]
# output: 5
print(maxProfitMemo(prices))