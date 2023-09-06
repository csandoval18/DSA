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
#           j        k
# arr[] = [-1,0,1,2,-1,-4]
# nums[k] = -(-1 + -1) => -(-2)
# nums[k] = 2


# (i != j != k)
# Cant pick element twice

# Ex:
# i,j = 2,-4
# nums[k] = -(2-4) = -(-2) = 2 => Need a 2 in the nums array
# Can not pick the 2 since it is the index of i and the elements can not be used twice

# To avoid duplication, the hash map must only contain the numbers within range of i and j