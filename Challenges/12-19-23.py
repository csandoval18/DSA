# 1913

# prod diff (a*b) - (c*d)
# pick w,x,y,z to maximize prod diff

# Thoughts
# So I gotta pick the pointers to maximize them. 
# I notice that I could change the order of (a*b) - (c*d) to get all possibilities
# for that curr set

# Dont need to do ^
# After observing the example given:
nums = [5,6,2,7,4]
# out: 34
# first pair (6,7) | second pair = (2,4)

# prod diff (a*b) - (c*d)
# So if you notice the left pair has the 2 maxes of the arr and the right pair that substracts 
# has the 2 min vals in the arr. 
# Solution 
# 1. Find 2 max nums in arr
# 2. Find 2 min nums in arr
# 3. Find product of 2 maxes and substract by product of 2 mins
# 4. return substraction

def getMaxAndPop(nums: [int]) -> [int]:
  maxVal = float('-inf')
  maxIdx = 0
  for i in range(len(nums)):
    if maxVal < nums[i]:
      maxVal = nums[i]
      maxIdx = i
  nums.pop(maxIdx)
  return maxVal
      
def getMinAndPop(nums: [int]) -> [int]:
  minVal = float('inf')
  minIdx = 0
  for i in range(len(nums)):
    if minVal > nums[i]:
      minVal = nums[i]
      minIdx = i
  nums.pop(minIdx)
  return minVal
      
def maxProductDifference(nums: [int]) -> int:
  print(nums)
  w = getMaxAndPop(nums)
  print(nums)
  x = getMaxAndPop(nums)
  print(nums)
  y = getMinAndPop(nums)
  print(nums)
  z = getMinAndPop(nums)
  print(nums)
  print(w,x,y,z)
  
  return (w*x) - (y*z)

print(maxProductDifference(nums))

def maxProductDifference(self, nums: List[int]) -> int:
  w = max(nums)
  nums.remove(w)
  x = max(nums)

  y = min(nums)
  nums.remove(y)
  z = min(nums)
  

# Fastest submission using some weird tricks to make compiler run faster
# sys.stdout = open('user.out', 'w')

# for nums in map(loads, sys.stdin):
#     largest = max(nums)
#     nums.remove(largest)
#     slargest = max(nums)

#     smallest = min(nums)
#     nums.remove(smallest)
#     ssmallest = min(nums)

#     nums.clear()
#     result = (largest * slargest) - (smallest * ssmallest)
#     print(dumps(result).replace(' ', ''))
# exit()