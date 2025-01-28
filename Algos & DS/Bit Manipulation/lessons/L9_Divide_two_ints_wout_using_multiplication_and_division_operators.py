# Divide by not using multiplication or division

class Solution:
  # Naive using addition
  '''
  dividend = 22
  divisor = 3
  
  Keep adding while sum <= dividend
  3 + 3 + 3 + 3 + 3 + 3 + 3 = 21
  cnt = 7
  '''
  def divide1(self, dividend: int, divisor: int) -> int: # TC: O(dividend) | SC: O(1)
    curr_sum, cnt = 0, 0
    
    while curr_sum + divisor <= dividend:
      cnt += 1
      curr_sum += divisor
    print(cnt)

  def divide2(self, dividend: int, divisor: int) -> int: # TC: O(dividend) | SC: O(1)
  
  
    