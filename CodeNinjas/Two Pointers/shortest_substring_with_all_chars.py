def shortestSubstring(s):
  m = {}
  for char in s:
    m[char] = m.get(char, 0) + 1

  temp_map = {}
  si = len(m)
  f_start, f_end, current, i, j = 0, 0, float('inf'), 0, 0

  while j < len(s):
    char_j = s[j]
    temp_map[char_j] = temp_map.get(char_j, 0) + 1

    if len(temp_map) == si:
      while temp_map[s[i]] > 1:
        temp_map[s[i]] -= 1
        i += 1

      if current > (j - i + 1):
        current = j - i + 1
        f_start = i
        f_end = j

    j += 1
  ans = s[f_start:f_end + 1]
  return ans
  
  
def shortest_substring_with_all_chars(s):
  char_cnt = {}
  required_chars = set(s)
  l, r = 0, 0
  min_len = float('inf')
  min_substr = ""
  
  while r < len(s):
    char_cnt[s[r]] = char_cnt.get(s[r], 0)+1
    r += 1
    
    while set(char_cnt.keys()) == required_chars:
      if r-l < min_len:
        min_len = r-l 
        min_substr = s[l:r]
      
      char_cnt[s[l]] -= 1
      if char_cnt[s[l]] == 0:
        del char_cnt[s[l]]
      
      l += 1
  return min_substr
    