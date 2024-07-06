# There are n people standing in a line labeled from 1 to n. 
# The first person in the line is holding a pillow initially. 
# Every second, the person holding the pillow passes it to the next person standing in the line. 
# Once the pillow reaches the end of the line, the direction changes, 
# and people continue passing the pillow in the opposite direction.

# For example, once the pillow reaches the nth person they pass it to the n-1'th person, then to the n-2'th person and so on.

# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.


class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    pillow = 1
    reverse = False
    
    while time > 0:
      print(pillow)
      if pillow == n:
        reverse = True
      elif pillow == 1:
        reverse = False
        
      if not reverse:
        pillow += 1
      else:
        pillow -= 1
    
      time -= 1
    return pillow
      
class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    i = 1
    direction = 1
    
    while time > 0:
      i += direction
      
      if i == n:
        direction = -1
      
      if i == 1:
        direction = 1
      time -= 1
  
    return i
      
# Using modulo to manage cycle
class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    direction = time // (n-1)
    
    if direction % 2 == 0:
      return 1 + time % (n-1)
    else:
      return n - (time % (n-1))

class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    left_to_right = True
    pos = 1
    for i in range(1, time+1):
      if left_to_right:
        pos += 1
      else:
        pos -= 1
      if i % (n-1) == 0:
        left_to_right = not left_to_right
    return pos
  
  
# n = 4
# time = 5
n = 18
time = 38

# Output: 2
s = Solution()
print("ans:", s.passThePillow(n, time))

# People pass the pillow in the following way: 
# 1 -> 2 -> 3 -> 4 -> 3 -> 2
# After 5 seconds, the 2nd person is holding the pilllow. 