'''
Find result of XOR operation in a range from l to r
'''
class Solution: # TC: O(N) | SC: O(1)
  def findXOR(self, l: int, r: int) -> int:
    res = 0
    
    for i in range(l, r):
      res ^= i
    return res


'''
n = 1            1 *
n = 2   1^2      3
n = 3   1^2^3    0
n = 4   1^2^3^4  4
n = 5            1 *
n = 6            7
n = 7            0
n = 8            8
n = 9            1 *

Notice how every 4 steps the answer is 1

n % 4 == 1  res = 1
n % 4 == 2  res = n+1
n % 4 == 3  res = 0
n % 4 == 0  res = n

1 % 4 = 1
2 % 4 = 2
3 % 4 = 3
4 % 4 = 0
5 % 4 = 1
6 % 4 = 2
7 % 4 = 3
8 % 4 = 0
9 % 4 = 1
10 % 4 = 2
11 % 4 = 3
12 % 4 = 0

def f(n: int) -> int:
  if n%4 == 1:
    return 1
  elif n%4 == 2:
      return n+1
  elif n%4 == 3:
    return 0
  else:
    return n

How to make it work in range:

(1^2^3) ^ (1^2^3^4^5^6^7)
 x x x     x x x
 f(l-1) ^ f(r)
'''

class Solution: # TC: O(1) | SC: O(1)
  def findXOR(self, l: int, r: int) -> int:
    def f(n: int) -> int:
      if n%4 == 1:
        return 1
      elif n%4 == 2:
        return n+1
      elif n%4 == 3:
        return 0
      else:
        return n
    
    return f(l-1) ^ f(r)
    