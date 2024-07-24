def isIsomorphic(s: str, t: str) -> bool:
  n = len(s)
  s2t = {}
  t2s = {}
  
  for i in range(n):
    schar = s[i]
    tchar = t[i]
    
    if schar in s2t:
      if s2t[schar] != tchar:
        return False
    else:
      s2t[schar] = tchar
    
    if tchar in t2s:
      if t2s[tchar] != schar:
        return False
    else:
      t2s[tchar] = schar
  return True

def isIsomorphic(s: str, t: str) -> bool:
  n = len(s)
  s2t = {}
  t2s = {}
  
  for i in range(n):
    if s[i] in s2t:
      if s2t[s[i]] != t[i]:
        return False
    else:
      s2t[s[i]] = t[i]
    
    if t[i] in t2s:
      if t2s[t[i]] != s[i]:
        return False
    else:
      t2s[t[i]] = s[i]
  return True

def isIsomorphic2(s: str, t: str) -> bool:
  ls = len(set(s))
  lt = len(set(t))
  lst = len(set(zip(s, t)))
  
  if ls == lt and ls == lst:
    return True
  else:
    return False