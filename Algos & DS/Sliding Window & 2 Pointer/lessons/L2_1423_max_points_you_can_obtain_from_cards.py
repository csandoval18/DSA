from typing import List

'''
              _______
cardPoints = [6,2,3,4,7,2,1,7,1] | k = 4
lsum = 15, rsum = 0
              _____           _
cardPoints = [6,2,3,4,7,2,1,7,1] | k = 4
lsum = 11, rsum = 1
              ___           ___
cardPoints = [6,2,3,4,7,2,1,7,1] | k = 4
lsum = 8, rsum = 8

'''

class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    rsum, lsum = 0, sum(cardPoints[:k])
    maxSum = lsum
    
    r = len(cardPoints)-1
    for l in range(k-1, -1, -1):
      lsum -= cardPoints[l]
      rsum += cardPoints[r]
      r = r-1
    
      maxSum = max(maxSum, lsum + rsum)
    return maxSum
    
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(sum(cardPoints[:k]))
# Output: 12