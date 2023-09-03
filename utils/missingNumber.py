# LC doesnt accept
def missingNumber(nums):
  nums.sort()
  tmp = nums[0]
  
  for i in range(1, len(nums)):
    if nums[i] != tmp+1:
      return tmp+1
    else:
      tmp = nums[i]

def missing_number(nums):
  i = 0
  
  for n in nums:
    if i != n:
      return i
    i += 1
  return i
  

nums = [3,0,1]
print(missingNumber(nums))
  