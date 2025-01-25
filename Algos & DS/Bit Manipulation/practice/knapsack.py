from typing import List


class Solution:
  def knapSack(self, val: List[int], wt: List[int], capacity: int) -> int:
    def f(i: int, profit: int, cap: int):
      if i == len(val):
        return profit
      
      take = f(i+1, profit+val[i], cap-wt[i])
      notTake = f(i+1, profit, cap)
      
      return max(take, notTake)
    
    return f(0, 0, capacity)

class Solution:
  def knapSack(self, val: List[int], wt: List[int], capacity: int) -> int:
    def f(i: int, profit: int, cap: int):
      # Was missing cases where capacity == 0 and capacity < 0
      if i == len(val) or cap == 0:
        return 0
      
      if wt[i] > cap:
        return f(i + 1, cap)
      
      take = f(i+1, profit+val[i], cap-wt[i])
      notTake = f(i+1, profit, cap)
      
      return max(take, notTake)
    return f(0, 0, capacity)
'''
val = [6,1,7,7]
wt =  [1,3,4,5]
         i

0Take
i = 0
p = 0 + 6 = 6
cap = 8 - 1 = 7

1Not take
i = 0 
p = 0
cap = 8

--------------

2Take 
i = 1
p = 6 + 1 = 7
cap = 7-3 = 4

3Not take
i = 1 
p = 6
cap = 7

4Take 
i = 1
p = 1
cap = 8 - 3 = 5

5Not take
i = 1
p = 0
cap = 8



'''

# val = [1,1]
# wt = [2,1]
# capacity = 3

val = [6,1,7,7]
wt =  [1,3,4,5]
capacity = 8

s = Solution()
print(s.knapSack(val, wt, capacity))