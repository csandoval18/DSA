from typing import List

# chatgpt
def maxProfitRecusirve(prices: List[int]):
  def f(day=0, buy=False):
    # Base case: If we've reached the end of the price list
    if day >= len(prices):
      return 0
    
    # Skip the day
    maxProfit = f(day+1, False)
    
    if buy:
      # If holding a stock, decide to sell it
      sellProfit = prices[day] + f(day+1, False)
      maxProfit = max(maxProfit, sellProfit)
    else:
      # If not holding a stock, decide to buy it
      buyProfit = -prices[day] + f(day+1, True)
      maxProfit = max(maxProfit, buyProfit)
    
    return maxProfit
  
  return f(0, 0)
  

def maxProfitMemo(prices: List[int]) -> int:
  def f(i: int, buy: bool, dp) -> int:
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
  dp[n][0] = dp[n][1] = 0
  
  for i in range(n-1, -1, -1):
    for buy in range(2):
      profit = 0
      
      if buy:
        # We can sell the stock
        profit = max(0 + dp[i+1][1], prices[i] + dp[i+1][0])
      else:
        # We can buy the stock 
        profit = max(0 + dp[i+1][0], -prices[i] + dp[i+1][1])
      dp[i][buy] = profit # Store the res in the dp table
    
  return dp[0][0]


def maxProfitSO(prices: List[int]) -> int:
  n = len(prices)
  nxt = [0,0]
  curr = [0,0]
  
  # Base condition: Initialize both 'nxt' and 'curr' to 0, 
  # as there are no more days to trade
  nxt[0] = nxt[1] = 0
  
  for i in range(n-1, -1, -1):
    for buy in range(2):
      profit = 0
      
      if buy:
        # We can sell the stock
        # profit = max(-prices[i] + f(i+1, 0, dp), # Take
        # 0 + f(i+1, 1, dp)) # Not take
        profit = max(0 + nxt[True], prices[i] + nxt[False])
      else:
        # We can buy the stock
        profit = max(0 + nxt[False], -prices[i] + nxt[True])
      curr[buy] = profit # Store the result in the curr list
    # Update nxt list
    nxt = curr
  
  return curr[0]
  
  
prices = [7,1,5,3,6,4]
# output: 7
print(maxProfitRecusirve(prices))
print(maxProfitMemo(prices))
print(maxProfitTab(prices))
print(maxProfitSO(prices))