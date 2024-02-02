# 2966. Divide Array Into Arrays With Max Difference

def divideArray(nums, k):
  nums.sort()
  result = []

  # Helper function to check if it's possible to form groups
  def canFormGroups():
    for i in range(0, len(nums), 3):
      group = nums[i:i+3]
      if len(group) < 3:
        return False
      if group[2] - group[0] > k:
        return False
    return True

  # Try to form groups
  if canFormGroups():
    for i in range(0, len(nums), 3):
      result.append(nums[i:i+3])
    return result
  else:
    return []
    