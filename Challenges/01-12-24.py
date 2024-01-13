# 1347. Minimum Number of Steps to Make Two Strings Anagram

# You are given 2 strings of the same len "s" & "t".
# In one step you can choose any char of "t" and replace it with another char

# Return the MIN number of steps to make "t" an anagram of "s"

# Anagram: string that contains the same chars (with different or same ordering)

from collections import Counter

def minStepsAttempt(s: str, t: str) -> int:
  s_chars = Counter(s)
  t_chars = Counter(t)
  min_steps = 0
  
  if s_chars == t_chars:
    return 0
    
  for char, cnt in t_chars.items():
    if char in s_chars:
      if cnt != s_chars[char] and cnt-s_chars[char] > 0:
        min_steps += cnt-s_chars[char]
    else:
      min_steps += 1
  return min_steps

def minSteps(s: str, t: str) -> int:
  # Count chars frequencies in both strings
  s_chars = Counter(s)
  t_chars = Counter(t)
  
  # Calculate the absolute diff in chars frequencies
  diff_cnts = s_chars - t_chars
  
  # The sum of absolute differences represents the min steps needed
  # min_steps = sum(abs(cnt) for cnt in diff_cnts.values())
  min_steps = 0
  for cnt in diff_cnts.values():
    min_steps += abs(cnt)
  return min_steps

s = "bab"
t = "aba"
# s = "leetcode"
# t = "practice"
# s = "anagram"
# t = "mangaar"

# Brakes attempt
# s = "gctcxyuluxjuxnsvmomavutrrfb"
# t = "qijrjrhqqjxjtprybrzpyfyqtzf"

print(minSteps(s, t))
