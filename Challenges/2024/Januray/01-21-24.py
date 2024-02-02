# 645. Set Mismatch
from collections import Counter
from typing import List

# Doesnt work ordering matters
def findErrorNumsHM(nums: List[int]) -> List[int]:
  res = [0, 0]
  hm = Counter(nums)
  
  for num in hm:
    if hm[num] == 2:
      res[0] = num
      if hm[num-1] not in hm:
        res[1] = num-1
        break
      if hm[num+1] not in hm:
        res[1] = num+1
        break

  return res 


def findErrorNumsMath(nums):
  n = len(nums)
  duplicate = sum(nums) - sum(set(nums))
  missing = n * (n+1) // 2 - sum(set(nums))
  return [duplicate, missing]


def findErrorNumsAbs(nums: [int]):
  n = len(nums)
  duplicate = -1
  missing = -1
  
  for num in nums:
    if nums[abs(num) - 1] < 0:
      duplicate = abs(num)
    else:
      nums[abs(num) - 1] *= -1
  
  for i in range(n):
    if nums[i] > 0:
      missing = i+1
  
  return [duplicate, missing]


# Favorite solution using set and then looping from 1 to n to find missing num
def findErrorNums(nums):
  seen = set()
  res = [0,0]
  
  for num in nums:
    if num in seen:
      res[0] = num
    seen.add(num)
  
  for i in range(1, len(nums)+1):
    if i not in seen:
      res[1] = i
      
  return res
  
  
nums = [2,2]
# nums = [1,2,2,4]
print(findErrorNums(nums))
# [2,2]
# output: [2,1]