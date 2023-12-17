# Agressive Cows -> (min dist between cows) is max

# You are given an arr consisiting o n ints which denote the position of a stall

def canPlaceCow(stalls, m, k):
  n = len(stalls)
  cntCows = 1 # Nums of cows placed
  last = stalls[0] # Position of last placed cow
  for i in range(1, n):
    if stalls[i] - last >= m:
      cntCows += 1 # Place next cow
      last = stalls[i] # Update the last location
    if cntCows >= k:
      return True
  return False

def aggressiveCows(stalls, k):
  n = len(stalls)
  stalls.sort()
  
  l, r = 1, stalls[n-1] - stalls[0]
  
  while l<=r:
    m = (l+r)//2
    if canPlaceCow(stalls, m, k):
      l = m+1
    else: r = m-1
  return r
  