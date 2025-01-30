class Solution:
  def countSetBits(self,n: int) -> int:
    cnt = 0
    
    while n > 0:
      cnt += n & 1 # Check if the rightmost bit is set (number is uneven)
      n = n >> 1 # Divide n by 2 (right shift every bit to the right)
    return cnt
      
  def countSetBits(self,n: int) -> int:
    cnt = 0
  
    while n != 0:
      n = n & (n-1) # Clears the right-most bit
      cnt += 1
    return cnt


'''
n = 13

13 / 2 = 6 rem 1
 6 / 2 = 3 rem 0 
 3 / 2 = 1 rem 1 
'''