from typing import List

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:

# - Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# - A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

# Return the number of teams you can form given the 

# Solution:
# The problem "1395. Count Number of Teams" is about counting the number of
# valid teams that can be formed from a list of soldiers, where each team consists of
# exactly three soldiers and satisfies either of the following conditions:

# 1. The triplet soldier's ratings are in increasing order.
# 2. The triplet soldier's ratings are in decreasing order.


# DP solution
class Solution:
  def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    if n < 3:
      return 0
    
    increasing = [0]*n
    decreasing = [0]*n
    count = 0
    
    for i in range(n):
      for j in range(i+1, n):
        if rating[i] < rating[j]:
          increasing[j] += 1
          count += increasing[i] # Increment count by the number of valid increasing pairs ending at i
        elif rating[i] > rating[j]:
          decreasing[j] += 1
          count += decreasing[i] # Increment count by the number of valid decreasing pairs ending at i
          
    return count

# Other Optimized Solution
class Solution:
  def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    if n < 3:
      return 0
    
    count = 0
    for i in range(1, n-1):
      less_left = greater_left = 0
      less_right = greater_right = 0
      
      for j in range(i): # Count soldiers on the left
        if rating[j] < rating[i]:
          less_left += 1
        elif rating[j] > rating[i]:
          greater_left += 1
      
      for k in range(i+1, n): # Count soldiers on the right
        if rating[k] < rating[i]:
          less_right += 1
        elif rating[k] > rating[i]:
          greater_right += 1
      
      count += less_left * greater_right + greater_left * less_right
    return count
    
    
rating = [2,5,3,4,1]
# Output: 3
s = Solution()
print(s.numTeams(rating))

rating = [2,1,3]
# Output: 0
s = Solution()
print(s.numTeams(rating))

rating = [1,2,3,4]
# Output: 0
s = Solution()
print(s.numTeams(rating))