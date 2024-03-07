from typing import List

def maxProfit(prices: List[int]) -> int:
  maxP = 0
  buy = prices[0]
  
  for i in range(1, len(prices)):
    cost = prices[i] - buy
    maxP = max(maxP, cost)
    buy = min(buy, prices[i])
  
  return maxP

prices = [7,1,5,3,6,4]
# output: 5
print(maxProfit(prices))

