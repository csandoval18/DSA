def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
  if len(jobDifficulty) < d:
    return -1
  
  cache = {}
  def dfs(i, d, curr_max):
    if i == len(jobDifficulty):
      return 0 if d == 0 else float('inf')
    elif d == 0:
      return float('inf')
    elif (i, d, curr_max) in cache:
      return cache[(i, d, curr_max)]
      
    curr_max = max(curr_max, jobDifficulty[i])
    res = min(dfs(i+1, d, curr_max), curr_max + dfs(i+1, d-1, -1))
    cache[(i, d, curr_max)] = res
    return res
  return dfs(0, d, -1)