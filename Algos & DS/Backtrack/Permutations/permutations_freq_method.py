from typing import List

# Does not work on arrays with repeating values
# We need to modify the for loop condition to check for dups
# as seen in the problem permutations 2
def permuteUnique(nums: List[int]) -> List[List[int]]:
  n = len(nums)
  freq = [0] * n
  res = []
  
  def backtrack(freq: List[int], ds: List[int]):
    if len(ds) == n:
      res.append(ds[:])
      return
      
    for i in range(n):
      if freq[i]:
        continue
      
      ds.append(nums[i])
      freq[i] = 1
      backtrack(freq, ds)
      freq[i] = 0
      ds.pop()
    
  backtrack(freq, [])
  return res


def permuteUnique(nums: List[int]) -> List[List[int]]:
  n = len(nums)
  freq = [0] * n
  res = []
  
  def bt(freq: List[int], ds: List[int]):
    if len(ds) == n:
      res.append(ds[:])
      return 
    
    for i in range(n):
      if freq[i]:
        continue
        
      ds.append(nums[i])
      freq[i] = 1
      bt(freq, ds)
      ds.pop()
      freq[i] = 0


# Visited method
def permute(nums: List[int]) -> List[List[int]]:
  res = []
  visited = set()

  def backtrack(permute, nums, visited):
    if len(permute) == len(nums):
      res.append(permute.copy())
      return
    
    for i in range(len(nums)):
      if i not in visited:
        visited.add(i)
        backtrack(permute + [nums[i]], nums, visited)  
        visited.remove(i)
  
  backtrack([], nums, visited)
  return res

def permute(nums: List[int]) -> List[List[int]]:
  res = []

  def dfs(idx: int, ds: List[int]): 
    if idx == len(nums): 
      res.append(ds[:])
      return 
    
    for i in range(len(nums)): 
      if nums[i] not in ds: 
        ds.append(nums[i])
        dfs(idx+1)
        ds.pop()
        
  dfs(0)
  return res
      
        
      
      
nums = [1,2,3]
print(permuteUnique(nums))