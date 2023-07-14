class Solution(object):
  def addDigits(self, num):
    arr = []
    x = num
    while x != 0:
      arr = [x%10] + arr
      x = x // 10