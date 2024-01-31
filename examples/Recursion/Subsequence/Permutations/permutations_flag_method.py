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
print()


def permuteRepeating(nums):
  n = len(nums)
  res = []
  freq = [0]*n
  
  def backtrack(ds, freq):
    if len(ds) == n:
      res.append(ds[:])
      return
    
    for i in range(n):
      ds.append(nums[i])
      freq[i] = 1
      backtrack(ds, freq)
      ds.pop()
      freq[i] = 0
  
  backtrack([], freq)
  return res

print(permuteRepeating(nums))
print()

def permute1(nums):
  n = len(nums) 
  res = []
  freq = [0]*n
  
  def backtrack(ds, freq):
    if len(ds) == n: 
      res.append(ds[:])
      return
    
    for i in range(n):
      if not freq[i]:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(ds, freq)
        ds.pop()
        freq[i] = 0
    
  backtrack([], freq)
  return res

print(permute1(nums))