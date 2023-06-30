# O(n^2)
def maxProfit1(prices):
  maxProfit = 0
  profit = 0
  
  for i in range(len(prices)):
    print("i:", i)
    for j in range(i, len(prices)):
      print("j:", j)
      profit = prices[j] - prices[i] 
      if profit > maxProfit:
        maxProfit = profit
  
  return maxProfit
  
# prices = [1,2]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))


def maxProfit(self, prices):
  l, r = 0, 1
  maxP = 0
  
  while r < len(prices):
    # Check left and right pointers values. If right pointer is greater than left (profit exists)
    if prices[l] < prices[r]:
      # then calc profit
      profit = prices[r] - prices[l]
      # check if profit is new max
      maxP = max(maxP, profit)
    else:
      # move left pointer to right position
      l = r
      
    # move 
    r += 1
  return maxP