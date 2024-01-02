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
  pass