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

  '''
  Reverse Engineering
            (3*7)
    3*(2^2 + 2^1 + 2^0)
  (3*2^2) + (3*2^1) + (3*2^0)
  '''
    
  def divide2(self, dividend: int, divisor: int) -> int: # TC: O(dividend) | SC: O(1)
    # Edge case: Overflow when dividing the minimum 32-bit integer by -1
    if dividend == -2**31 and divisor == -1:
      return 2**31-1
      
    # Determine the sign of the result
    sign = (dividend < 0) == (divisor < 0)
    
    # Work with abs values
    n = abs(dividend)
    d = abs(divisor)
    res = 0
    
    # Outer loop: Keep subtracting multiples of the divisor from the dividend
    while n >= d:
      tmp = d
      cnt = 1
      # Inner loop: Find the largest multiple of the divisor that fits into the remaining dividend
      while (tmp << 1) <= n: # Double the divisor until it exceeds the remaining dividend
        tmp <<= 1 # Double the divisor
        cnt <<= 1 # Double the corresponding quotient
      
      # Add the quotient to the result and subtract the multiple from the dividend
      res += cnt
      n -= tmp
    
    # Apply the sign to the result
    if not sign:
      res = -res
    
    # Handle overflow by clamping the result to 32-bit integer range
    if res > 2**31-1:
      return 2**31-1
    if res < -2**31:
      return -2**31
      
    return res
    
  def divide3(self, dividend: int, divisor: int) -> int: # TC: O(dividend) | SC: O(1)
    if dividend == -2**31 and divisor == -1:
      return 2**31 - 1
    
    sign = (dividend < 0) == (divisor < 0)
    
    n = abs(dividend)
    d = abs(divisor)
    res = 0
    
    while n >= d:
      temp = d
      cnt = 1
      
      while (temp << 1) <= n:
        temp <<= 1
        cnt <<= 1
      
      res += cnt
      n -= temp
    
    if not sign:
      res = -res
    
    if res > 2**31 - 1:
      return 2**31 - 1
    if res < -2**31:
      return -2**31
    
    return res