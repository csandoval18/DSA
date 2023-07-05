def singleNumber(nums):
  hm = {}
  
  for i, n in  enumerate(nums):
    if n not in hm:
      hm[n] = i
    else: hm.pop(n)
  
  return list(hm.keys())[0]
      
    
  
print(singleNumber([2,2,1]))

