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

def appendChars(s: str, t: str):
  s_pointer = 0
  t_pointer = 0
  
  while s_pointer < len(s) and t_pointer < len(t):
    if s[s_pointer] == t[t_pointer]:
      t_pointer += 1
    s_pointer += 1
  
  return len(t) - t_pointer

def appendChars(s: str, t: str):
  s_pointer = 0
  t_pointer = 0 
  
  while s_pointer < len(s) and t_pointer < len(t):
    if 

s = "coaching"
t = "coding"
print(appendCharacters(s, t))
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

s = "z"
t = "abcde"
# Output: 5
# Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
# Now, t is a subsequence of s ("zabcde").
# It can be shown that appending any 4 characters to the end of s will never make t a subsequence.