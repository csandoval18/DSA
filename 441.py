class Solution(object):
    def arrangeCoins(self, n):
      filledRows = 0
      coins = n
      
      for row in range(n):
        print(coins, row)
        coins -= row
        if coins > row:
          filledRows += 1
        else:
          return filledRows
        

ans = Solution()
n = 8
print(ans.arrangeCoins(n))

# O(n) Linear
class Solution(object):
    def arrangeCoins(self, n):      
      row = 1
      res = 0

      while row <= n:
        n -= row
        res += 1
        row += 1
      return res
    
# O(log(n)) Binary Search
class Solution(object):
    def arrangeCoins(self, n):      
      l, r = 0, n

      while l <= r:
        m = (l + r) // 2;

        if n >= m * (m + 1) // 2:
          l = m + 1;
          
        r = m - 1;
        return l - 1; 