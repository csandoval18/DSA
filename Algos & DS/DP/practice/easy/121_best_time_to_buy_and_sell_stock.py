from typing import List

class SolutionLinear:
  def maxProfit(self, prices: List[int]) -> int:
    maxP = 0
    buy = prices[0]
    
    for i in range(1, len(prices)):
      curr_profit = prices[i] - buy
      maxP = max(maxP, curr_profit)
      buy = min(buy, prices[i])
    
    return maxP

      
class SolutionRec:
  def maxProfit(self, prices: List[int]) -> int:
    def helper(i: int, minPrice: int, maxProfit: int) -> int:
      # Base case: if we've processed all the prices, return the max profit
      if i == len(prices):
        return maxProfit
      
      # Update the min price seen so far
      minPrice = min(minPrice, prices[i])
      # Update the min price if we sell on day i
      currProfit = prices[i] - minPrice
      maxProfit = max(maxProfit, currProfit)
      # Recur to the next day
      return helper(i+1, minPrice, maxProfit)
    # Start the recursion from day 0, with no transactions made yet
    return helper(0, float('inf'), 0)
  

class SolutionRec:
  def maxProfit(self, prices: List[int]) -> int:
    def helper(i: int, minPrice: int, maxProfit: int) -> int:
      if i == len(prices):
        return maxProfit
      
      minPrice = min(minPrice, prices[i])
      currProfit = prices[i] - minPrice
      maxProfit = max(maxProfit, currProfit)
      return helper(i+1, minPrice, maxProfit)
    return helper(0, float('inf'), 0)


from typing import List

class SolutionMemo:
  def maxProfit(self, prices: List[int]) -> int:
    # Memoization table
    n = len(prices)
    memo = [[-1] * 2 for _ in range(n)]
    
    def helper(i: int, purchased: bool) -> int:
      # Base case: if we've processed all days
      if i == n:
        return 0
      
      # Check if result is already computed
      if memo[i][int(purchased)] != -1:
        return memo[i][int(purchased)]
      
      if purchased:
        # Two choices: sell the stock today or not sell
        sell = prices[i] + helper(i + 1, False)  # Sell today, then cannot hold stock anymore
        notSell = helper(i + 1, True)  # Keep holding the stock
        memo[i][1] = max(sell, notSell)  # Store the maximum profit after selling or not selling
      else:
        # Two choices: buy the stock today or skip it
        buy = -prices[i] + helper(i + 1, True)  # Buy today, then must hold stock
        notBuy = helper(i + 1, False)  # Skip buying the stock
        memo[i][0] = max(buy, notBuy)  # Store the maximum profit after buying or skipping
      
      # Return the computed value for this state
      return memo[i][int(purchased)]
    # Start with day 0, and we have not purchased yet
    return helper(0, False)


class SolutionDP:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n == 0:
      return 0
    
    dp = [0]*n
    minPrice = prices[0] 
    
    for i in range(1, n):
      minPrice = min(minPrice, prices[i])
      dp[i] = max(dp[i-1], prices[i] - minPrice)
    return dp[-1]


# class SolutionRec: # Allows multiple purchases and sells
#   def maxProfit(self, prices: List[int]) -> int:
#     def helper(i: int, purchased: bool) -> int:
#       # Base case: reached end of prices list
#       if i == len(prices):
#         return 0
      
#       # Case where the stock is purchased
#       if purchased:
#         sell = prices[i] + helper(i+1, False) # Sell and move to the next day without holding
#         notSell = helper(i + 1, True) # Do not sell, continue holding the stock
#         return max(sell, notSell)
        
#       # Case where we haven't purchased a stock yet
#       buy = -prices[i] + helper(i+1, True) # Buy and move to the next  day holding the stock
#       notBuy = helper(i+1, False) # Skip buying, move to the next day without holding
#       return max(buy, notBuy)
    
#     # Start recursion from day 0 without holding any stock
#     return helper(0, False)