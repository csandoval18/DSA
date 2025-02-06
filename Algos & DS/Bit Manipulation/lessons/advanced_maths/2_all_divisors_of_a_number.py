class Solution:
  def print_divisors(self, N: int):
    st = set()
   
    for i in range(N):
      if N % i == 0:
        st.add(i)
    return st
      
  def print_divisors(self, N: int):
    res = []
    
    for i in range(1, int(N**0.5)):
      if N % i == 0:
        res.append(i)
        if N // i != i: # Avoid adding the same divisor twice for perfect squares | Ex: N = 36 = 6 * 6
          res.append(N // i)
    return res
    
  def print_divisors(self, N: int):
    divisor = set() # A set can also be used to avoid adding duplicate divisors in perfect squares
    
    for i in range(1, int(N**0.5)+1):
      if N % i == 0:
        divisor.add(i)
        divisor.add(N // i)
    
    res = sorted(res)
    for num in res:
      print(num, end=" ")

N = 20
# Output: 1 2 4 5 10 20
# Explanation: 20 is completely divisible by 1, 2, 4, 5, 10 and 20.

N = 36
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]

s = Solution()
print(s.print_divisors(N))
