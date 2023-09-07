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


def threeSum(nums):
  triplets = []
  
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      for k in range(j+1, len(nums)):
        if nums[i] + nums[j] + nums[k] == 0:
          triplet = [nums[1], nums[j], nums[k]]
          triplet.sort()
          # Adds only unique solutions
          if triplet not in triplets:
            triplets.append(triplet)

  return triplets

nums = [-1,0,1,2,-1,-4]

# Optimized solution

# nums[i] + nums[j] + nums[k] = 0
# nums[k] = - (nums[i] + nums[j])

# Ex:
#          j        k
# nums = [-1,0,1,2,-1,-4]
# nums[k] = -(-1 + -1) => -(-2)
# nums[k] = 2


# (i != j != k)
# Cant pick element twice

# Ex:
# i,j = 2,-4
# nums[k] = -(2-4) = -(-2) = 2 => Need a 2 in the nums array
# Can not pick the 2 since it is the index of i and the elements can not be used twice

# To avoid duplication, the hash map must only contain the numbers within range of i and j

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

# Increase j index
# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i                j         k 

# Moving k back causes a duplicate to occur, so we need to move j out of 0s range

# Increase j index
# nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#          i                      j     k 
