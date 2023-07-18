class Solution(object):
    def addDigits(self, num):
      if num % 10 != 0 and num // 10 == 0:
        return num
      elif num == 0:
        return 0
        
      arr = []
      tmp = num
      
      while tmp != 0:
        arr = [tmp % 10] + arr
        tmp = tmp // 10
      
      total = 0
      for n in arr:
        total += n
      
      self.addDigits(total)