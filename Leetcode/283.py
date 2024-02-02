class Solution(object):
  def moveZeroes(self, nums):
    count = 0
    i = 0
    
    while i != len(nums)-1:
      if nums[i] == 0:
        count += 1
        nums.pop(i)
        i -= 1
      i += 1
    
    for i in range(count):
      nums.append(0)
    
    return nums


nums = [0,0,1]
sol = Solution()
print(sol.moveZeroes(nums))

        