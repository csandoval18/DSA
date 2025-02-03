'''
  n = 13

  13 / 2 = 6 rem 1
  6 / 2 = 3 rem 0 
  3 / 2 = 1 rem 1 
  
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
  
This does not ask for the bits of an integer. It asks to find the total bits set from a range of 1 to n (inclusive).
def countSetBits(self,n: int) -> int:
'''

class SolutionAttempt:
  def countBits(self, n: int) -> int: # TC: O(N log(N)) Too slow to be accepted
    cnt = 0
    
    while n > 0:
      cnt += n & 1
      n = n >> 1
    return cnt
    
  def countSetBits(self,n):
    # code here
    # return the count
    res = 0
    for i in range(1, n+1):
      res += self.countBits(i)
    return res

class Solution:
  def countSetBits(self, n: int) -> int: # TC: O(log(N)) | SC: O(1)
    total_set_bits = 0
    
    while n > 0:
      # Find the highest power of 2 <= n set as x
      x = 0
      while (1 << x) <= n:
        x += 1
      x -= 1
      
      # Handle the case when x = 0
      if x == 0:
        total_set_bits += 1
        break  # Exit the loop since n is now 0
      
      # Calculate the set bits up to (2^x - 1)
      set_bits_up_to_x = x * (1 << (x - 1))
      # Calculate the set bits in the MSB for numbers from 2^x to n
      msb_set_bits = n - (1 << x) + 1
      # Add to the total set bits
      total_set_bits += set_bits_up_to_x + msb_set_bits
      
      # Update n to the remaining numbers
      n = n - (1 << x)
    return total_set_bits

class Solution:
  def countSetBits(self, n: int) -> int:
    res = 0
    
    while n > 0:
      x = 0
      while (1 << x) <= n:
        x += 1
      x -= 1
      
      if x == 0:
        res += 1
        break
      
      set_bits_up_to_x = x * (1 << (x - 1))
      msb_set_bits = n - (1 << x) + 1
      res += set_bits_up_to_x + msb_set_bits
      n = n - (1 << x)
    return res

# Example usage:
n = 51
s = Solution()
s.countSetBits(n)