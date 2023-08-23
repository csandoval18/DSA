# for i in range(2, 0):
#   print("hello")

# arr = [1,2,3,4,5]
# print("arr len:", len(arr))


def maxProfit(prices):
  l = 0
  maxP = 0

  for r in range(1, len(prices)):
    # Check if price of previous day in pointer "l" is smaller than pointer "r"
    # If it is smaller this indicates that there is a profit since you could buy
    # stock at a cheaper prices the previous day "l" and sell the current day "r"
    if prices[l] < prices[r]: 
      # Calculate profit made 
      profit = prices[r] - prices[l]
      # Update new max profit
      maxP = max(maxP, profit)
    # This part below is necessary
    # It updates the left pointer to be the right since the price in pointer "l" is greater than 
    # in pointer "r". This means that there is no profit to be made therefore "l" need to be updated to the 
    # lower price which is pointer "r" in that iteration
    else:
      l = r
  return maxP

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
