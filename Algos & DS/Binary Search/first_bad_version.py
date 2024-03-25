# API recreation
def isBadVersion(version):
  bad = 4
  
  if version < bad: return False
  else: return True
  
def firstBadVersion(self, n):
  l = 1
  r = n

  while l <= r:
    m = (l+r)//2

    mVer = isBadVersion(m)
    if mVer == True and isBadVersion(m-1) == False:
        return m
    
    elif isBadVersion(l) == False and mVer == False:
        l = m+1
    
    elif mVer == True and isBadVersion(r) == True:
        r = m-1
  return -1