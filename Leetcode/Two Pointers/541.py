def reverseStr(s: str, k: int) -> str:
  l, r = 0, k-1
  chars = list(s)

  while r < len(chars):
    chars[l], chars[r] = chars[r], chars[l]
    l += 2*k
    r += 2*k
    if len(chars)-r+1 < k:
      while r < len(chars):
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r += 1
  return "".join(chars)
  
s = "abcdef"
k = 3

print(reverseStr(s, k))

# 2 while loops
def reverseStr(s: str, k: int) -> str:
  s_list = list(s)
  i = 0
  
  while i < len(s_list):
    start = i
    end = min(i + k - 1, len(s_list) - 1)
    
    # Reverse the current group in-place
    while start < end:
      s_list[start], s_list[end] = s_list[end], s_list[start]
      start += 1
      end -= 1
    
    i += 2*k
  
  result = ''.join(s_list)
  
  return result

# Using for loop
def reverseStr(s: str, k: int) -> str:
    s_list = list(s)
    
    for i in range(0, len(s_list), 2 * k):
      l, r = i, min(i + k - 1, len(s_list) - 1)
      
      while l < r:
        s_list[l], s_list[r] = s_list[r], s_list[l]
        l += 1
        r -= 1
    
    result = ''.join(s_list)
    return result
    
    
# Using slicing
def reverseStr(s: str, k: int) -> str:
  res = ""

  for i in range(0, len(s), 2*k):
    res += s[i:i+k][::-1] + s[i+k:i+2*k]
  return res