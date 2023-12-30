def intections(arr1: [int], n: int, arr2: [int], m: int):
  st = set()
  res = []
  
  for num in arr2:
    if num not in st:
      st.add(num)
  
  for num in arr1:
    if num in st:
      res.append(num)
      st.remove(num)
  
  return res