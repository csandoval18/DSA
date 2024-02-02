class Solution(object):
  def fizzBuzz(self, n):
    ans = []
    i = 1
    
    while i <= n:
      if i % 3 == 0 and i % 5 == 0:
        ans.append("FizzBuzz")
      elif i % 3 == 0:
        ans.append("Fizz")
      elif i % 5 == 0:
        ans.append("Buzz")
      else:
        ans.append(str(i))
      i += 1
    return ans


ans = Solution()
print(ans.fizzBuzz(3))
    
    