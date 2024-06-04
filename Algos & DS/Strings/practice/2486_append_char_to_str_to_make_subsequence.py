# Given 2 strings 's' & 't'. 
# Return the min num of chars that need to be appended to the end of 's' so that 't' becomes a subsequence of 's'.

def appendCharacters(s: str, t: str) -> int:
  s_pointer = 0
  t_pointer = 0
  
  while s_pointer < len(s) and t_pointer < len(t):
    if s[s_pointer] == t[t_pointer]:
      t_pointer += 1
    s_pointer += 1
  
  return len(t) - t_pointer