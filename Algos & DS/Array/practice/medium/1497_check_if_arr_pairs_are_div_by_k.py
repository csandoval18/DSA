from typing import List

# Modulo Solution>
# The problem asks us to check whether we can pair elements in such a way that the 
# sum of each pair is divisible by k. Using remainders is 
# a key idea because if two numbers a and b leave remainders r_a and r_b when divided by k, 
# then their sum (a + b) will be divisible by k only if:
'''
(r_a + r_b) % k == 0
'''

class Solution:
  def canArrange(self, arr: List[int], k: int) -> bool:
    rem_cnt = [0] * k
    
    # Calculate remainder frequencies
    for num in arr:
      rem = num % k
      rem_cnt[rem] += 1
    
    # Check if pairs can be made
    for i in range(1, k):
      if rem_cnt[i] != rem_cnt[k-i]:
        return False
    
    # Special case: remainder 0, there should be an even count
    if rem_cnt[0] % 2 != 0:
      return False
      
    return True

# Hash map solution  
class Solution:
  def canArrange(self, arr: List[int], k: int) -> bool:
    rem_hm = {}
    
    # Calculate the remainder for each element and update the frequency in the map
    for num in arr:
      rem = num % k
      if rem < 0:
        rem += k # Ensure positive remainders
      rem_hm[rem] = rem_hm.get(rem, 0) + 1
    
    # Now, check if we can form valid pairs
    for rem in rem_hm:
      if rem == 0:
        # For remainder 0, we need an even count
        if rem_hm[rem] % 2 != 0:
          return False
      else:
        # For remainder `i`, we need a matching remainder `k - i`
        complement = k - rem
        if rem_hm.get(complement, 0) != rem_hm[rem]:
          return False
    return True
      
    
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
# Output: true