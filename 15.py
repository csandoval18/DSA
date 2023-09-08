# Brute force

# Q's
# Which element can be my first?
# Which element can be my second?
# Which element can be my third?

# arr = [-1,0,1,2,-1,-4]
#         1 2 3 3  3  3
#         1   2 3  3  3
#         1     2  3  3
#         1        2  3
#           1 2 3  3  3
#           1   2  3  3
#           1      2  3
#             1 2  2  3
#               1  2  3

# O(n^3)
def threeSum(nums):
  n = len(nums)
  triplets = set()
  
  for i in range(n):
    for j in range(i+1, n):
      for k in range(j+1, n):
        if nums[i] + nums[j] + nums[k] == 0:
          triplet = [nums[i], nums[j], nums[k]]
          triplet.sort()
          # Adds only unique solutions
          triplets.add(tuple(triplet))

  res = [list(item) for item in triplets]
  return res
  
# Chatgpt brute force
def threeSumBruteForce(nums):
  n = len(nums)
  triplets = []
  nums.sort()
  
  # Dont need the n-2 and n-1 in i and j but they cut off avoids
  # those iterations that are not useful for the solution
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if nums[i] + nums[j] + nums[k] == 0:
          triplet = [nums[i], nums[j], nums[k]]
          if triplet  not in triplets:
            triplets.append(triplet)
  return triplets

# Optimized solution

# nums[i] + nums[j] + nums[k] = 0
# nums[k] = - (nums[i] + nums[j])

# Ex:
#          i        j
# nums = [-1,0,1,2,-1,-4]
# nums[k] = -(-1 + -1) => -(-2)
# nums[k] = 2


# (i != j != k)
# Cant pick same element twice

# Ex:
# i,j = 2,-4
# nums[k] = -(2-4) = -(-2) = 2 => Need a 2 in the nums array
# Can not pick the 2 since it is the index of i and the elements can not be used twice

# To avoid duplication, the hash map must only contain the numbers within range of i -> j (exclusive)

# O(n^2 * log(# of triplets))
def three_sum_better_appraoch(nums):
  res = set()
  
  for i in range(len(nums)):
    hashset = set()
    for j in range(i+1, len(nums)):
      # Calculate the 3rd element:
      k = -(nums[i] + nums[j])
      
      # Find the element in the set
      if k in hashset:
        tmp = [nums[i], nums[j], k]
        tmp.sort()
        res.add(tmp)
      hashset.add(nums[j])
      
  return res
        

# Optimal 2 pointer approach

# nums[i] + nums[j] + nums[k]
# target = 0

# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i  j                         k

# -2 -2 + 2 = -2 => Need to increase the value to get the target 0

# Increase j index
# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i  j  j  j  j  j j           k

# -2 -1 + 2 = -1
# -2 + 0 + 2 = 0 = result

# Increase j index or reduce k index depending on the formula value for k
# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i                j         k 


# In this case moving k back causes a duplicate to occur, so we need to move j out of 0s range

# Increase j index
# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i                      j   k 

# When j surpasses k then we stop that loop & continue

# O(NlogN) + O(n^2) = O(n^2)
# Space complexity: # of quadruplets. O(1) no extra space is used other than result
def threeSumOptimized(nums):
  n = len(nums)
  res = []
  nums.sort()
  
  for i in range(n):
    # Remove duplicates by checking if i non 0 index (starting index) 
    # value is equal to its last iteration value
    if i != 0 and nums[i] == nums[i-1]:
      continue
    
    # Moving 2 pointers:
    j = i+1
    k = n-1
    
    while j < k:
      total_sum = nums[i] + nums[j] + nums[k]
      
      if total_sum < 0:
        j += 1
      elif total_sum > 0:
        k -= 1
      else: # total_sum == 0
        tmp = [nums[i], nums[j], nums[k]]
        res.append(tmp)
        j += 1
        k -= 1
        
        # Skip duplicates
        while j < k and nums[j] == nums[j-1]:
          j += 1
        while j < k and nums[k] == nums[k+1]:
          k -= 1
          
  return res 
  
nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]

print(threeSumBruteForce(nums))
        