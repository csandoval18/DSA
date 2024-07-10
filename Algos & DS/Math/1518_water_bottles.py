# There are 'numBottles' water bottles that are initially full of water.  
# You can exchange 'numExchange' empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turn it into an empty bottle

# Given the two integers 'numBottles' and 'numExchange', return the maximum number of water bottles you can drink.


import math


class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    res = 0
    emptyBottles = 0

    while numBottles > 0:
      res += numBottles
      emptyBottles += numBottles
      numBottles = emptyBottles // numExchange
      emptyBottles = emptyBottles % numExchange

    return res

# numBottles, numExchange = 9, 3
numBottles, numExchange = 15, 4
s = Solution()
print(s.numWaterBottles(numBottles, numExchange))
    