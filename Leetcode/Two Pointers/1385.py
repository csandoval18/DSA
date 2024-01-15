from typing import List

# Distance val is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i] -arr2[j] <= d|
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
  res = 0
  
  for num1 in arr1:
    is_valid = True

    for num2 in arr2:
      if abs(num1-num2) <= d:
        is_valid = False
        break
    if is_valid:
      res += 1
  return res

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))