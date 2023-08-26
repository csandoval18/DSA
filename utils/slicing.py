nums = [1,2,3,4]
# Output = [24,12,8,6]

for i in range(len(nums)):
  print("Iteration ", i)
  print(nums[:i])
  print(nums[i+1:])
  print("\n")