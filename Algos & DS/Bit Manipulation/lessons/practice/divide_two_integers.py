class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    # Handle overflow case
    if dividend == -2**31 and divisor == -1:
      return 2**31-1
    
    # Determine the sign of the result
    sign = (dividend < 0) == (divisor < 0)
    
    # Work with absolute values
    n = abs(dividend)
    d = abs(divisor)
    
    res = 0
    while n >= d:
      tmp = d
      cnt = 1
      
      while (tmp << 1) <= n:
        tmp <<= 1
        cnt <<= 1
        
        while (tmp << 1) <= n:
          tmp <<= 1
          cnt <<= 1
        res += cnt
        n -= tmp
        # Add the count to the result and substract the tmp from the dividend
        res += cnt
        n -= tmp
    
    # Apply the sign to the result
    if not sign:
      res = -res
    # Handle overflow
    if res > 2**31-1:
      return 2**31-1
    if res < -2**31:
      return -2**31
    return res