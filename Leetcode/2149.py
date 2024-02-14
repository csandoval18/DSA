# Optimal O(n) uses 2 pointers to keep track of negatives and positives 
# in initiated array with len(nums)

# Uses extra space O(n)
def rearrangeArray(nums):
  n = len(nums)
  res = [0] * n
  posIndex = 0 
  negIndex = 1
  
  for i in range(n):
    if nums[i] < 0:
      res[negIndex] = nums[i] 
      negIndex += 2
    else:
      res[posIndex] = nums[i]
      posIndex += 2
  return res
  
  
# For cases where there is more + then - or viseversa,
# We need to backtrack to the less optimized solution of getting neg and pos arrays with
# present order and then inserting them into a new array in a correct order 

def alternateNumber(nums):
  pos, neg = [], []
  n = len(nums)
  
  # Add - & + numbers to corresponding array 
  for num in nums:
    if num >= 0:
      pos.append(num)
    else:
      neg.append(num)
  
  # If there are more + elements than - elements
  if len(pos) > len(neg):
    # Edit original array with pos and neg array elements
    # i needs to be multiplied by 2 because it needs to increase
    # by 2 and begin at 0, then only way to that is by multiplying
    
    # i             i
    # 0 * 2 = 0  |  0 * 2 + 1 = 1
    # 1 * 2 = 2  |  1 * 2 + 1 = 3
    # 2 * 2 = 4  |  2 * 2 + 1 = 5
    for i in range(len(neg)):
      nums[i*2]  = pos[i]
      nums[i*2+1] = neg[i]
    
    # Add remaining elements of bigger array
    rem_idx = len(neg) * 2
    for i in range(len(neg), len(pos)):
      nums[rem_idx] = pos[i]
      rem_idx += 1
  
  # Else if there are more - elements than + elements
  # len(pos) < len(neg)
  else:
    for i in range(len(pos)):
      nums[i*2] = pos[i]
      nums[i*2+1] = neg[i]
      
      # Add remaining elements of bigger array
      rem_idx = len(pos) * 2
      for i in range(len(pos), len(neg)):
        nums[rem_idx] = neg[i]
        rem_idx += 1
  
  return nums
        
# Optimized SC: O(n), TC: O(1)      
def rearrangeArray(nums):
  i, j = 0, 1  # i for positive, j for negative
  n = len(nums)

  while i < n and j < n:
    # Find the next positive element (if missing, break)
    while i < n and nums[i] >= 0:
      i += 2

    # Find the next negative element (if missing, break)
    while j < n and nums[j] < 0:
      j += 2

    # Swap positive and negative elements
    if i < n and j < n:
      nums[i], nums[j] = nums[j], nums[i]

  return nums

    
      
  
  