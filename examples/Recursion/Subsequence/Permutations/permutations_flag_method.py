from typing import List

def permute(nums: [int]) -> [[int]]:
  n = len(nums)
  res = []
  ds = []
  
  def backtrack(freq: List[int]):
    if len(ds) == n:
      res.append(ds[:])
      return
      
    for i in range(n):
      if freq[i] == False:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(freq)
        freq[i] = 0
        ds.pop()
    
  freq = [0] * n
  backtrack(freq)
  return res

nums = [1,2,3]
print(permute(nums))


def permute(nums: [int]) -> [[int]]:
  def backtrack(freq: [int]):
    if n == len(ds):
      res.append(ds[:])
      return 
    
    for i in range(n):
      if freq[i] == 0:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(freq)
        freq[i] = 0
        ds.pop()
  
  n = len(nums)
  ds = []
  freq = [0]*n
  res = []
  backtrack(freq)
  return res
  
def permute(nums):
  n = len(nums)
  res = []
  ds = []
  
  def backtrack(freq):
    if n == len(ds):
      res.append(ds[:])
      return
    
    for i in range(n):
      if freq[i] == 0:
        ds.append(nums[i])
        ds[i] = 1
        backtrack(freq)
        ds.pop()
        ds[i] = 0
        
  freq = [0]*n     
  backtrack(freq)
  return res
  
  
  
  
  
  
  
def permute(nums):
  n = len(nums)
  ds = []
  freq = [0]*n
  res = []
  
  def backtrack(freq):
    if n == len(ds):
      res.append(ds.copy())
      return
    
    for i in range(n):
      if freq[i] == 0:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(freq)
        freq[i] = 0
        ds.pop()

  backtrack(freq) 
  return res
  