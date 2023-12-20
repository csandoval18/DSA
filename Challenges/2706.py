def buyChoco(prices: [int], money: int) -> int:
  res = money
  minVal = min(prices)
  res -= minVal
  prices.remove(minVal)
  minVal = min(prices)
  res -= minVal 
    
  if res < 0:
    return money
  else:
    return res

prices = [3,2,3]
money = 3
print(buyChoco(prices, money))