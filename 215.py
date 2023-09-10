def findKthLargest(nums, k):
  nums.sort()
  i = len(nums)-1
  k_flag = 1

  while 0 <= i:
    if k_flag == k:
      return nums[i]
      
    i -= 1
    k_flag += 1
    
nums = [1,2,2,3,3,4,5,5,6,7,8,8,8,8]
k = 4

print(findKthLargest(nums, k))