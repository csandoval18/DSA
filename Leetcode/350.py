class Solution(object):
  def intersect(self, nums1, nums2):
    hm = {}
    res = []

    # Count occurrences of each element in nums1
    for i in nums1:
      hm[i] = hm.get(i, 0) + 1

    # Find common elements in nums2 and decrement counts in hm
    for i in nums2:
      # If num does not exist in num_count or its count is 0, it means either the element doesn't 
      # exist in nums1 or we have already exhausted all occurrences of the element in nums1. 
      # In such cases, we do not consider that element as part of the intersection.
      if i in hm and hm[i] > 0:
        res.append(i)
        hm[i] -= 1

    return res


# If num exists in num_count and its count is greater than 0, 
# it indicates that the element is present in both arrays and we haven't used up all its occurrences in nums1. 
# We include that element in the intersection and decrement its count in num_count to track the usage.