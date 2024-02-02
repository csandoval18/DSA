# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# res = 15

# weights = [1,2,3,4,5,6,7,8,9,10]
# l = max(weights)
# r += num for num in weights

# BF
def findDaysBF(weights: [int], cap: int) -> int:
  days = 1 # First day
  load = 0
  n = len(weights)
  
  for i in range(n):
    if load + weights[i] > cap:
      days += 1 # Move to next day
      load = weights[i] # Load the weight
    else: # Load the weight on the same day
      load += weights[i]
  return days

def leastWeightCapacity(weights: [int] , d: int) -> int:
  # Find the max and the summation
  maxi = max(weights)   
  summation = sum(weights)
  
  for i in range(maxi, summation+1):
    if findDaysBF(weights, i) <= d:
      return i
  
  # dummy return statement 
  return 
    
      
# Optimal Binary Search on  ans
def shipWithinDays(weights: [int], days: int) -> int:
  def calcDaysSum(weight, cap): 
    days = 1
    load = 0
    for i in range(len(weights)):
      if load+weights[i] > cap:
        days += 1 # Move to the next day
        load = weights[i] # Load the weight
      else:
        # Load the weight on the same day
        load += weights[i]
    return days

  l, r = max(weights), sum(weights)
  
  while l<=r:
    m = (l+r)//2
    numOfDays = calcDaysSum(weights, m)
    if numOfDays <= days:
      # Eliminate right half
      r = m-1
    else:
      l = m+1
  return l
      
      
      