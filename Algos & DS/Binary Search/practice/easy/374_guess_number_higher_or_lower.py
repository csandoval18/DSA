class Solution:
    
  def guessNumber(self, n: int) -> int:
    def guess(n: int) -> int:
      answer = 7
      if n < answer:
        return 1
      elif n > answer:
        return -1
      elif n == answer:
        return 0
    # ---------------------------------------------    
    l, r = 1, n

    while l <= r:
      m = (l+r)//2

      if guess(m) == 0:
        return m
      elif guess(m) == 1:
        l = m+1
      elif guess(m) == -1:
        r = m-1
    return -1
