def firstUniqChar(s):
  """
  :type s: str
  :rtype: int
  """
  hm = {}
  repeating = {}
  
  for i, n in enumerate(s):
    if n not in hm and n not in repeating:
      hm[n] = i
    
    elif n in hm and n not in repeating:
      repeating[n] = i
      hm.pop(n)
      
  print(hm)
  return min(list(hm.values())) if len(list(hm.values())) > 0 else -1
  
s = "loveleetcode"
#ans = o
print(firstUniqChar(s)) 