from collections import defaultdict

def findMatrix(nums: [int]) -> [[int]]:
  dd = defaultdict(int)
  res = []
  
  for num in nums:
    row = dd[num]
    if len(res) == row:
      res.append([])
    
    res[row].append(num)
    dd[num] += 1
  return res
    