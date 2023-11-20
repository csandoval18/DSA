from typing import List

def maxProduct(nums: List) -> int:
  n = len(nums)
  pre, suf = 1, 1
  maxProd = float('-inf')
  
  for i in range(n):
    if pre == 0:
      pre = 1
    if suf == 0:
      suf = 1
    
    pre = pre * nums[i]
    suf = suf * arr[n-i-1]
    maxProd = max(maxProd, pre, suf)
  return maxProd
    
arr = [2,3,-2,4]
print(maxProduct(arr))

