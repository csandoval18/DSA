def intections(arr1: [int], n: int, arr2: [int], m: int):
  arr2_set = set()
  res = []
  
  for num in arr2:
    if num not in arr2_set:
      arr2_set.add(num)
  
  for num in arr1:
    if num in arr2_set:
      res.append(num)
  
  return res