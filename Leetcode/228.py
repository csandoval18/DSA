class Solution(object):
  def summaryRanges(self, nums):
    res = []
    
    for i in range(3):
      m = max(nums)
      res.append(m)
      nums.remove(m)
    return res

ans = Solution()
ans.summaryRanges()
    