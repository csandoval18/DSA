# bloomDay = [1,10,3,10,2]
# m = 3 -> you make m bouquets
# k = 1 -> you need to use k adjacent flowers from the garden

# The garden consists of n flowers, the ith flower will bloom 
# in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the min number of days you need to wait to be able to make m bouquets from the garden.
# It is impossible to make m bouquets return -1

# Brute Force
from ast import List


def possible1(arr, day, m, k):
  n = len(arr)
  cnt = 0
  noOfB = 0
  
  # count the num of bouquets
  for i in range(n):
    if arr[i] <= day:
      cnt += 1
    else:
      noOfB = cnt // k
      cnt = 0
  noOfB += cnt // k
  return noOfB >= m

def roseGarden(arr, k, m):
  val = m * k
  n = len(arr)
  if val > n:
    return -1 # impossible case
  # find max and min
  mini = float('inf')
  maxi = float('-inf')
  for i in range(n):
    mini = min(mini, arr[i])
    maxi = max(maxi, arr[i])
  
  for i in range(mini, maxi+1):
    if possible(arr, i, m, k):
      return i
  return -1

# Optimal
def possible(arr, day, m, k):
  n = len(arr) # size of the array
  cnt = 0
  noOfB = 0
  # count the number of bouquets
  for i in range(n):
    if arr[i] <= day:
      cnt += 1
    else:
      noOfB += cnt // k
      cnt = 0
  noOfB += cnt // k
  return noOfB >= m
  
def minDays(bloomDay: [int], m: int, k: int) -> int:
  val = m*k
  n = len(bloomDay) 
  if val > n: 
    return -1 # impossible case
    
  # find max and min
  mini = float('inf')
  maxi = float('-inf')
  for i in range(n):
    mini = min(mini, bloomDay[i])
    maxi = max(maxi, bloomDay[i])
  
  # apply binary search
  l, r = mini, maxi
  
  while l<=r:
    mid = (l+r) // 2
    if possible(bloomDay, mid, m, k):
      r = m-1
    else:
      l = m+1
  return l

bloomDay = [7,7,7,7,13,12,7]
k = 3
m = 2
print(minDays(bloomDay, k, m))

# ///////////////////////////////////////////////////////////////////////////////
# bloomDay = [1,10,3,10,2]
# m = 3 -> you make m bouquets
# k = 1 -> you need to use k adjacent flowers from the garden

class Solution:
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    def possible(bloomDay, mid, m, k):
      n = len(bloomDay) # size of the array
      cnt = 0
      noOfB = 0
      # count the number of bouquets
      for i in range(n):
        # If bloomday is lower than mid then the plant will bloom within the given m day
        if bloomDay[i] <= mid:
          cnt += 1
        # Else we need to reset cnt to 0
        else:
          noOfB += cnt // k
          cnt = 0
      noOfB += cnt // k
      return noOfB >= m

    val = m*k
    n = len(bloomDay) 
    if val > n: 
      return -1 # impossible case
        
    # find max and min
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
      mini = min(mini, bloomDay[i])
      maxi = max(maxi, bloomDay[i])
    
    # apply binary search
    l, r = mini, maxi
    
    while l<=r:
      mid = (l+r) // 2
      if possible(bloomDay, mid, m, k):
        r = mid-1
      else:
        l = mid+1
    return l