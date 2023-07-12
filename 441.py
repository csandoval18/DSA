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

class Solution(object):
    def arrangeCoins(self, n):      
      i =1;
      res = 0;

      while i<=n{
        n -= i;
        res += 1;
        i += 1;
      } 