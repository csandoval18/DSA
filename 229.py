def majorityElementBF(nums):
  n = len(nums)
  res = []
  
  for i in range(n):
    # Selected element is nums[i]
    # Checking if res is empty or if current element val is already 
    # in the res array
    if len(res) == 0 or res[0] != nums[i]:
      cnt = 0
      for j in range(n):
        # Counting frequency of nums[i]
        if nums[j] == nums[i]:
          cnt += 1
      # Check if frequency is greater than n/3
      if cnt > n//3:
        res.append(nums[i])
    if len(res) == 2:
      break
  return res
  
  
def majorityElementBetter(nums):
  hm = {}
  
  for num in nums:
    hm[num] = hm.get(num, 0) + 1
    
  return hm
    
  
  
# Return all elements that appear more than ⌊ n/3 ⌋ (floor) | (ceil) = ⌈ x ⌉
nums = [3,2,3]
# print(majorityElement(majorityElement(nums)))
print(majorityElementBetter(nums))