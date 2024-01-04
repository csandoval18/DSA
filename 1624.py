def maxLengthBetweenEqualCharacters(s: str) -> int:
  n = len(s)
  if n <= 2:
    return 0
    
  l, r = 0, n-1
  maxLen = 0
  
  while l < n:
    while l < r and s[l] != s[r]:
      r -= 1
      
    if s[l] == s[r]:
      curr_len = (r-l+1)-2
      maxLen = max(curr_len, maxLen)

    r = n-1
    l += 1
  
  if maxLen > 0:
    return maxLen
  else:
    return -1


# s = "aa"
# s = "abca"
# s = "cbzxy"
# Error forgot to reset r to n-1
s = "scayofdzca"
print(maxLengthBetweenEqualCharacters(s))