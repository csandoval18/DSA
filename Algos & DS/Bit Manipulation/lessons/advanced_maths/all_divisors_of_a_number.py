class Solution:
  def print_divisors(self, N: int):
    res = []
    res.append(N)
    res.append(1)
    
    for i in range(2, int(N**0.5)):
      if N % i == 0:
        res.append(i)
    
    return res

N = 20
# Output: 1 2 4 5 10 20
# Explanation: 20 is completely divisible by 1, 2, 4, 5, 10 and 20.
s = Solution()
print(s.print_divisors(N))