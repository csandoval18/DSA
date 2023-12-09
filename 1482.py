# bloomDay = [1,10,3,10,2]
# m = 3 -> you make m bouquets
# k = 1 -> you need to use k adjacent flowers from the garden

# The garden consists of n flowers, the ith flower will bloom 
# in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the min number of days you need to wait to be able to make m bouquets from the garden.
# It is impossible to make m bouquets return -1

# Brute Force
def possible(arr, day, m, k):
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
def possible1(arr, day, m, k):
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
  
def roseGarden(arr, k, m):
  val = m*k
  n = len(arr)
  if val > n:
    return -1 #impossible case

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