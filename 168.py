class Solution(object):
  def convertToTitle(self, columnNumber):
    result = ""
    
    while n > 0:
      n -= 1
      result = chr(n % 26 + ord('A')) + result
      n //= 26
    return result
      