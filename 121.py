# O(n^2)
def maxProfit1(prices):
  maxProfit = 0
  profit = 0
  
  for i in range(len(prices)):
    for j in range(i+1, len(prices)):
      profit = prices[j]-prices[i] 
      
      if profit > maxProfit:
        maxProfit = profit
  
  return maxProfit

def maxProfit(prices):
  l, r = 0, 1
  maxP = 0
  
  while r < len(prices):
    # Check left and right pointer values. If right pointer is greater than left (profit exists)
    if prices[l] < prices[r]:
      # then calc profit
      profit = prices[r] - prices[l]
      # check if profit is new max
      maxP = max(maxP, profit)
    else:
      # move left pointer to right position
      l = r
    r += 1
  return maxP
  
# prices = [1,2]
prices = [7,1,5,3,6,4]
print(maxProfit1(prices))
print(maxProfit(prices))