class Solution(object):
  def titleToNumber(self, columnTitle):
    result = 0
    n = len(columnTitle)
    
    for i in range(n):
      # Get the numerical value of the current character
      value = ord(columnTitle[n - i - 1]) - ord('A') + 1
      
      # Calculate the contribution of the current character to the result
      result += value * (26 ** i)
    
    return result