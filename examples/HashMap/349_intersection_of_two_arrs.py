from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> int:
  count1, count2 = {}, {}
  
  for num in nums1:
    count1[num] = count1.get(num, 0)+1
  
  for num in nums2:
    count2[num] = count2.get(num, 0)+1
  
  res = []
  for num in count1:
    if num in count2:
      res.append(num)
  
  return res


# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))