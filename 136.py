def singleNumber(self, nums):
  res = 0 # n ^ 0 = n
  for n in nums:
    res = n ^ res
  return res
  x
  