def minCost(colors: str, neededTime: [int]) -> int:
  stack = []
  res = 0
  
  for i in range(len(colors)):
    if stack and colors[stack[-1]] == colors[i]:
      if neededTime[stack[-1]] < neededTime[i]:
        res += neededTime[stack.pop()]
      else:
        res += neededTime[i]
        continue
    res.append(i)
  return res