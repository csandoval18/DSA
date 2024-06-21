# There is a bookstore owner that has a store open for n minutes. Every minute, some
# number of customers enter the store. You are given an integer array customers of length
# n where customers[i] is the number of the customer that enters the store at the start of
# the ith minute and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy. 
# You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy 
# during the ith minute, and is 0 otherwise

# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the day.

from typing import List


class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)

    # Step 1: Calculate initial satisfaction without using the technique
    initital_satisfaction = sum(customers[i] for i in range(n) if grumpy[i] == 0)
    
    # Step 2: Calculate the potential additional satisfaction using the technique
    additional_satisfaction = 0
    for i in range(minutes):
      if grumpy[i] == 1:
        additional_satisfaction += customers[i]
    
    max_additioinal_satisfaction = additional_satisfaction
    
    # Use sliding window to find the max additional satisfaction in any 'minute' window
    for i in range(minutes, n):
      if grumpy[i] == 1:
        additional_satisfaction += customers[i]
      if grumpy[i-minutes] == 1:
        additional_satisfaction -= customers[i - minutes]
      
      max_additioinal_satisfaction = max(max_additioinal_satisfaction, additional_satisfaction)
      
    # Total satisfied customers is the sum of initially satisfied and the best additional satisfaction
    return initital_satisfaction + max_additioinal_satisfaction


customers = [1,0,1,2,1,1,7,5] 
grumpy = [0,1,0,1,0,1,0,1] 
minutes = 3
# Output: 16
s = Solution()
print(s.maxSatisfied(customers, grumpy, minutes))