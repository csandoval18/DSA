# Brute Force O(n^2)
def nextGreaterElementBF(nums: [int], n: int) -> [int]:
  res = []
  
  for i in range(n-1):
    res_len = len(res)
    for j in range(i+1, n):
      if nums[i] < nums[j]: 
        res.append(nums[j])
        break
    # Check to see if no bigger number found by comparing res arr size
    if res_len == len(res):
      res.append(-1)
  # Last index will always be -1 since there is no elements to the right
  res.append(-1) 
  return res

def nextGreaterElement(nums: [int], n: int) -> [int]:
  greater = []
  stack = []

  for i in reversed(nums):
    if len(greater)==0:
      stack.append(-1)
      greater.append(i)
    else:
      while len(greater)!=0 and greater[-1]<=i:
        greater.pop()

      if len(greater)!=0 and greater[0]>i:
        stack.insert(0,greater[-1])
        greater.append(i)

      else:
        stack.insert(0,-1)
        greater.append(i)
  return stack
  
nums = [1,5,3,4,2]
print(nextGreaterElement(nums, len(nums)))
# 5 -1 4 -1 -1


# Optimal O(N)
def nextGreaterElement(arr: [int], n: int) -> [int]:
  res = [0]*n
  stack = []
  for i in range(n-1,-1,-1):
    while len(stack) and arr[i] >= stack[-1]:
      stack.pop()
    if len(stack) == 0:
      res[i] =- 1
    else:
      res[i] = stack[-1]
    stack.append(arr[i])
  return res
