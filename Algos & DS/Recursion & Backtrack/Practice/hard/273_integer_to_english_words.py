class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0: # Handling edge case 0
      return "Zero"
    
    # Mapping numbers to words
    below_20 = [  
        "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen"
    ]
    tens = [
        "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def rec(n: int) -> str:
      if n == 0:
        return ""
      elif n < 20:
        return below_20[n-1] + " "
      elif n < 100:
        return tens[n // 10 - 2] + " " + rec(n % 10)
      else:
        return below_20[n // 100 - 1] + " Hundred " + rec(n % 100)
    
    res = ""
    for i in range(len(thousands)): 
      # 123 % 1000 = 123, 8000 % 1000 = 0. This basically checks that num is a number in chunks of 3 digits at a time for recurssion
      if num % 1000 != 0:        
        res = rec(num % 1000) + thousands[i] + " " + res
      num //= 1000 # Removes last 3 digits. Ex: 123,456,789 // 1000 = 123,456
    
    return res.strip() # strip method of a string removes leading and trailing white spaces
    
num = 123
# Output: "One Hundred Twenty Three"
s = Solution()
print(s.numberToWords(num))