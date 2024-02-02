def isAnagram(s, t):
  hm = {}
  
  # Needed for case such as s = "a", t = "ab"
  # Hash map cannot recognize the error
  if len(s) != len(t):
    return False
  
  # Get count of each char in string s
  for i in range(len(s)):
    char = s[i]
    hm[char] = hm.get(char, 0) + 1
  
  for j in range(len(t)):
    char = t[j]
    if char in hm:
      hm[char] -= 1
      if hm[char] == 0:
        hm.pop(char)
  
  print(hm)

  return True if len(list(hm.keys())) == 0 else False
  
s = "aacc"
t = "ccac"

print(isAnagram(s, t))