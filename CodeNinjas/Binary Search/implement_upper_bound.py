def lowerBound(arr: [int], n: int, x: int) -> int:
  l = 0
  r = n-1
  res = n
  
  while l<=r:
    m = (l+r) // 2
    print("l:", arr[l])
    print("m:", arr[m])
    print("r:", arr[r])
    
    if arr[m] > x:
      res = m
      print("res:", res)
      r = m-1
    else:
      l = m+1
    print()
  print("l:", arr[l])
  print("m:", arr[m])
  print("r:", arr[r])
  return res

n = 5
nums = [1,4,7,8,10]
x = 7
print(lowerBound(nums, n, x))
