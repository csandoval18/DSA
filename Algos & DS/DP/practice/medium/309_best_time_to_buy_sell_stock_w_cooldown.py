from typing import List


class SolutionRec:
  def maxProfit(self, prices: List[int]) -> int:
    def helper(i: int, purchased: int, cooldown: int) -> int:
      # Base case: reached end of prices list
      if i == len(prices):
        return 0
      
      if cooldown != 0:
        helper(i+1, 0, cooldown-1)
        
      # Case where the stock is purchased
      if purchased:
        sell = prices[i] + helper(i+1, 0, 1) # Sell and move to the next day without holding
        notSell = helper(i + 1, 1, 0) # Do not sell, continue holding the stock
        return max(sell, notSell)
        
      # Case where we haven't purchased a stock yet
      buy = -prices[i] + helper(i+1, 1, 0) # Buy and move to the next  day holding the stock
      notBuy = helper(i+1, 0, 0) # Skip buying, move to the next day without holding
      return max(buy, notBuy)
    
    # Start recursion from day 0 without holding any stock
    return helper(0, 0, 0)


class SolutionMemo:
  def maxProfit(self, prices: List[int]) -> int:
    def helper(i: int, purchased: int, cooldown: int) -> int:
      if i == n:
        return 0
      
      if dp[i][purchased][cooldown] != -1:
        return dp[i][purchased][cooldown]
        
      if cooldown != 0:
        return helper(i+1, 0, cooldown-1)
        
      if purchased:
        sell = prices[i] + helper(i+1, 0, 1)
        notSell = helper(i + 1, 1, 0)
        dp[i][purchased][cooldown] = max(sell, notSell)
        return dp[i][purchased][cooldown]
        
      buy = -prices[i] + helper(i+1, 1, 0)
      notBuy = helper(i+1, 0, 0)
      dp[i][purchased][cooldown] = max(buy, notBuy)
      return dp[i][purchased][cooldown]
    
    n = len(prices)
    dp = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(n)]
    return helper(0, 0, 0)
    
    
class SolutionDP:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n == 0:
      return 0
      
    # Intialize DP table: dp[i][purchased][cooldown]
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
    
    # Base case: After the last day, the profit is 0 for any state
    for purchased in range(2):
      for cooldown in range(2):
        dp[n][purchased][cooldown] = 0
    
    # Fill the DP table from the end to the beginning 
    for i in range(n-1, -1, -1):
      for purchased in range(2):
        for cooldown in range(2):
          if cooldown != 0:
            dp[i][purchased][cooldown] = dp[i+1][0][cooldown-1]
          else:
            if purchased:
              # Option to buy or skip
              sell = prices[i] + dp[i+1][0][1]
              notSell = dp[i+1][0][0]
              dp[i][purchased][cooldown] = max(sell, notSell)
            else:
              # Option to buy or skip
              buy = -prices[i] + dp[i][1][0]
              notBuy = dp[i][0][0]
              dp[i][purchased][cooldown] = max(buy, notBuy)
              
    # The answer is the max profit starting at day 0, with no stock purchased and no cooldown
    return dp[0][0][0]
            