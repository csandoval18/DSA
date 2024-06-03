def scoreOfString(s: str) -> int:
  res = 0
  l = 0
  
  for r in range(1, len(s)):
    res += abs(ord(s[l]) - ord(s[r]))
    l += 1
    
  return res
  
def scoreOfString2(s: str) -> int:
  res = 0
  
  for i in range(len(s)-1):
    res += abs(ord(s[i]) - ord(s[i+1]))
  
  return res

s = "hello"
print(scoreOfString(s))
print(scoreOfString2(s))