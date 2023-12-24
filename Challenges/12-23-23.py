# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. 
# In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. 
# For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

# "0100"
# Out: 1

def minOperationsAttempt1(self, s: str) -> int:
  n = len(s)

  if n == 1:
    return 0

  res = 0
  l, r = 0, 1

  while r < n:
    if s[l] == s[r]:
      res += 1
    l += 2
    r += 2
  return res
  
# Remember strings are immutable in python
# My attempts dont work because there are 2 possibilities a string that starts with 0 or 1
# Notice how in the question they ask for the MIN of changes needed to make the string "alternating"
# This means that I would need to check the possibilities of starting with 0 and 1 and then returning the min

def minOperationsAttempt2(s: str) -> int:
  arr = list(s)
  n = len(arr)
  if n == 1:
    return 0
    
  res = 0
  for i in range(1, n, 1):
    if arr[i] == arr[i-1]:
      res += 1
      if arr[i] == "1":
        arr[i] = "0"
      else:
        arr[i] = "1"
  return res
        

      
def minOperationsA(s: str) -> int:
  c0 = 0
  c1 = 0

  for i in range(len(s)):
    if i % 2 == 0: 
      # c0 wants 0, c1 wants 1
      if s[i] == '0':
        c1 += 1
      else:
        c0 += 1
    else:
      # c0 wants 1, c1 wants 0
      if s[i] == '1':
        c1 += 1
      else:
        c0 += 1
  
  return min(c0, c1)
  
def minOperations(self, s: str) -> int:
  count_start0 = 0
  count_start1 = 0

  # Iterate through the string with two pointers
  for i in range(len(s)):
    # Check for mismatches starting with '0'
    if s[i] != str(i % 2):
      count_start0 += 1

    # Check for mismatches starting with '1'
    if s[i] != str((i + 1) % 2):
      count_start1 += 1

  # Return the minimum count between the two starting positions
  return min(count_start0, count_start1)
  
# Fastest
def minOperations(s: str) -> int:
  change_1 = 0
  flag = True

  for char in s:
    print("char:", char)
    print("flag:", flag)
    print("change_1:", change_1)
    if flag == (char == "0"):
      change_1 += 1
      
    flag = not flag
    print("\n")
  print("change_1", change_1)
  print("", change_1)
  return min(change_1, len(s) - change_1)     
  
  
s = "10010100"
# 01234567
# 10010100
# Expected 3 got 1
print(minOperations(s))


# c1 = 0
# fl = T

# "10010100"
#  c

# 
# "10010100"
#  c