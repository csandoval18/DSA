from collections import Counter

def customSortString(self, order: str, s: str) -> str:
  # Count the occurrence of each character in str
  s_cnt = Counter(s)
  res = []

  # Build the result string based on the order, consuming the character counts
  for char in order:
    if char in s_cnt:
      res.append(char * s_cnt[char])
      del s_cnt[char] # Remove the char from char_count once added to result
      
  # Add remaining characters not in order to the end of the result
  for char, count in s_cnt.items():
    res.append(char * count)
  
  return ''.join(res)