# So binary search is not applicable to the coding ninjas problem
# They probably made a mistake since the arr is not sorted 
# and they want you to return the next greater to the right side
# it it was just the next greater in general it would work, but 
# since they want the next greater ON THE RIGHT SIDE of the og unsorted
# arr, making bs very complicated to use

def nextGreaterElement(arr: [int], n: int) -> [int]:
  arr.sort()
  ans = []
  print(arr)
  
  for num in arr:
    x = binarySearch(arr, num)
    print("x:", x)
    print("x+1:", x+1)
    print("arr[x]:", arr[x])
    
    if x < n-1 and x != -1:
      ans.append(arr[x+1])
    else:
      ans.append(-1)
  
  return ans
  
def binarySearch(arr: [int], t):
  print("bs arr:", arr)
  n = len(arr)
  l, r = 0, n-1
  res = -1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] == t:
      res = m
      l = m+1
    if arr[m] <= m:
      l = m+1
    else:
      r = m-1
  return res


a = [7,12,1,20]
print(nextGreaterElement(a, len(a)))