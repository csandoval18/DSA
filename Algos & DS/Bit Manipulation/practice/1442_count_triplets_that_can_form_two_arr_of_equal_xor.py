from typing import List

def countTriplets(arr: List[int]) -> List[int]:
  n = len(arr)
  prefixXOR = [0]*(n+1)
  
  # Compute prefix XOR array
  for i in range(n):
    prefixXOR[i+1] = prefixXOR[i] ^ arr[i]
  
  cnt = 0
  # Check for each pair (i, k)
  for i in range(n):
    for k in range(i+1, n):
      if prefixXOR[i] == prefixXOR[k+1]:
        cnt += k-i
  
  return cnt