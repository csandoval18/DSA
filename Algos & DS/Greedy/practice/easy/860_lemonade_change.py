from typing import List


# Each lemonade costs $5
# Customers standing in queue and order one at a time
# Each customer only buys 1 lemonade and pays with either a $5, $10, $20 bill. 
# Every customer's bill is $5. Provide the correct change to each.

# * You do not have any change in hand at the start

# Given an integer array bills where bills[i] is the bill the ith customer pays, return 
# true if you can provide every customer with the correct change, or false otherwise.


class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    fives, tens = 0, 0
    
    for bill in bills:
      if bill == 5:
        fives += 1
      elif bill == 10:
        if fives == 0:
          return False
        fives -= 1
        tens += 1
      else:
        if tens > 0 and fives > 0:
          tens -= 1
          fives -= 1
        elif fives >= 3:
          fives -= 3
        else:
          return False
    return True