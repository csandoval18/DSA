class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
    
        if len(nums) >= 3:
          for i in range(len(nums)):
              m = max(nums)
              res.append(m)
              nums.remove(m)
          return max(res[2])
        else:
          return max(nums)
          
class Solution(object):
  def thirdMax(self, nums):
    # initialize 3 variables for 3 max numbers
    # they are initialized to float(-inf) tohandle the case where there are no 
    # distinct max numbers in the array
    first = second = third = float('-inf')
    
    # For each number we compare it with the current top 3 max nums
    for n in nums:
      # If it is greater than first, we update all 3 variables to maintain the ordering of the top 3 nums
      if n > first:
        third = second
        second = first
        first = n
    
      elif n > second and n < first:
        third = second
        second = n
      elif n > third and n< second:
        third = n
    
    if third != float('-inf'):
      return third
    else:
      return first
    
    
    
    
