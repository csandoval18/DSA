# L     M     R
# 1,1,2,3,3,4,4
# 0 1 2 3 4 5 6
# Output: 2


def getSingleElement(arr: [int]) -> int:
  l, r = 0, len(arr)-1

  while l<r:
    m = (l+r)// 2

    # Check if the single element is on the left or right
    if m % 2 == 1:
      m -= 1

    # Adjust the search space based on whether the single element is on the left or right
    if arr[m] == arr[m+1]:
      l = m+2
    else:
      r = m

  return arr[l]
  

# In each iteration of the loop, the middle element mid and its adjacent element mid + 1 
# are compared. If mid is an odd index (i.e., mid % 2 == 1), mid is adjusted to point to 
# the previous even index (mid -= 1). This ensures that the comparison is always done 
# with an even index.

# Now, if nums[mid] == nums[mid + 1], it means the single element is on the right side, 
# and the search space is adjusted accordingly (left = mid + 2). If nums[mid] != nums[mid + 1], 
# it means the single element is on the left side, and the search space is adjusted 
# accordingly (right = mid).

# By using left < right as the loop condition, the algorithm ensures that the search space is 
# reduced appropriately, and the loop exits when the search space contains only the 
# single element.