from typing import List

# Recursion solution does not work since the complexity is too high

# Remember there is 2 methods to find subsequences using a freq dp and swapping: 

# BF 1 freq ds
def getPermutationBFFreq(n: int, k: int) -> str:
  nums = [i for i in range(1, n+1)]
  res = []
  freq = [0]*n
  
  def backtrack(freq: List[int], ds: List[int]) -> None:
    if len(ds) == n:
      res.append(ds[:])
      return
    
    for i in range(n):
      if not freq[i]:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(freq, ds)
        ds.pop()
        freq[i] = 0
        
  backtrack(freq, [])
  res.sort()
  return "".join(map(str, res[k-1]))

# BF swap
def getPermutatitonBFSwap(n: int, k: int) -> str:
  nums = [i for i in range(1, n+1)]
  res = []
  
  def backtrack(idx: int) -> None:
    if idx == n:
      res.append(nums[:])
      return
    
    for i in range(idx, n):
      nums[i], nums[idx] = nums[idx], nums[i]
      backtrack(idx+1)
      nums[i], nums[idx] = nums[idx], nums[i]
    
  backtrack(0)
  res.sort()
  return "".join(map(str, res[k-1]))


# Optimal Solution
def getPermutation(n: int, k: int) -> str:
  fact = 1
  nums = []
  for i in range(1, n):
    fact *= i
    nums.append(i)
  nums.append(n)
  
  res = "" 
  k -= 1
  while True:
    res += str(nums[k // fact])
    nums.pop(k//fact)
    
    if not nums:
      break
    
    k %= fact
    fact //= len(nums)
  return res
    
print(getPermutationBFFreq(3, 3))
print()
print(getPermutatitonBFSwap(3, 3))
print()
print(getPermutation(3,3))