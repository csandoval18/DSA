def twoSum(numbers, target):
  hm = {}
  
  for i, n in enumerate(numbers):
    x = target - n
    
    if x not in hm:
      hm[n] = i
    else:
      return [hm[x]+1, i+1]
      
  return None