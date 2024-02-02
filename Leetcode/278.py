
# API recreation
def isBadVersion(version):
  bad = 4
  
  if version < 4: return False
  else: return True
  
def firstBadVersion(n):
  l = 1
  r = n
  
  while l <= r:
    m = (l+r)//2
    
    mVer = isBadVersion(m)
    if mVer == True and isBadVersion(m-1):
      return m
    elif isBadVersion(l) == False and mVer == False:
      l = m+1
    elif mVer == True and isBadVersion(r) == True:
      r = m-1
    
  return -1
  
n = 5
print(firstBadVersion(n))
      