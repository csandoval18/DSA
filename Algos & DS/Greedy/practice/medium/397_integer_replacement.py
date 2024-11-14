class Solution:
  def integerReplacement(self, n: int) -> int:
    steps = 0
    while n > 1:
      if n % 2 == 0:
        n //= 2
      elif n == 3 or ((n >> 1) & 1) == 0:
        # If n is 3 or if n - 1 has fewer 1-bits in its binary representation
        n -= 1
      else:
        # Otherwise, increment to make it divisible by 2
        n += 1
      steps += 1
    return steps
