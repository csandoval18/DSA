from typing import List


class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    rsum = 0
    lsum = sum(cardPoints[:k])
    maxSum = lsum
    
    j = n-1 # i = left index | j = right index
    for i in range(k-1, -1, -1):
      lsum -= cardPoints[i]
      rsum += cardPoints[j]
      j = j-1
    
      maxSum = max(maxSum, lsum + rsum)
    
    return
    
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(sum(cardPoints[:k]))
# Output: 12