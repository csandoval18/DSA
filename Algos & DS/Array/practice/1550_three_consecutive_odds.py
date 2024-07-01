from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
      n = len(arr)
      consecutive_odds = 0
      
      for num in arr:
        if num % 2 == 1:
          consecutive_odds += 1
        else: 
          consecutive_odds = 0
            
        if consecutive_odds == 3:
          return True
          
      return False
      
# arr = [1,2,34,3,4,5,7,23,12]
arr = [1,1,1]
s = Solution()
print(s.threeConsecutiveOdds(arr))
