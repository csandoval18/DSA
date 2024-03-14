def maxProfit(prices):
  l = 0
  max_profit = 0
  
  for r in range(len(prices)):
    if prices[r] < prices[l]:
      l = r
      continue
      
    max_profit = max(max_profit, prices[r] - prices[l])
  
  return max_profit
  
# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(maxProfit(prices))