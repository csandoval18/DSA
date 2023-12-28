# 1578. Minimum Time to Make Rope Colorful

# Alice has n balloons arranged on a rope.
# You are given a 0-index str 'colors' where 'colors[i]' is the colors of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be the same color,

def minCost(colors: str, neededTime: [int]) -> int:
  n = len(colors)
  stack = []
  ans = 0
  
  for i in range(n):
    if stack and colors[stack[-1]] == colors[i]:
      if neededTime[stack[-1]] < neededTime[i]:
        ans += neededTime[stack.pop()]
      else:
        ans += neededTime[i]
        continue
    stack.append()
  return ans
      
        
      
    