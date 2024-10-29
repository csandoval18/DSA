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
      
      minPrice = min(minPrice, prices[i]) # Update the min price seen so far
      currProfit = prices[i] - minPrice # Update the min price if we sell on day i
      maxProfit = max(maxProfit, currProfit) # Recur to the next day
      return helper(i+1, minPrice, maxProfit)
    return helper(0, float('inf'), 0) # Start the recursion from day 0, with no transactions made yet


class SolutionMemo:
  def maxProfit(self, prices: List[int]) -> int:
    def helper(i: int, minPrice: int, maxProfit: int) -> int:
      if i == len(prices):
        return maxProfit
      
      minPrice = min(minPrice, prices[i])
      currProfit = prices[i] - minPrice
      maxProfit = max(maxProfit, currProfit)
      dp[i] = helper(i+1, minPrice, maxProfit)
      return dp[i]
      
    dp = [-1] * len(prices) 
    return helper(0, float('inf'), 0)


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