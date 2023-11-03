from typing import *

# Inversions = number of pairs of i, j such that i < j and a[i] > a[j]
# A = [5,3,2,1,4]
# (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), and (3,4)

# BF O(n^2)
def numberOfInversionsBF(a: List[int], n) -> int:
  res = 0
  for i in range(n):
    for j in range(i+1, n):
      # a[i], a[j] can be a pair
      if a[i] > a[j]:
        res += 1
  return res
  
  
# Optimal O(n log n)
def numberOfInversions(a, n):   
  
        