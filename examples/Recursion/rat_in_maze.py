from typing import List

def rat_in_maze(maze: List[List[int]]):
  n = len(maze)
  m = len(maze[0])
  res = []
  visited = [[0 for _ in range(n)] for _ in range(n)]
  
  def backtrack(i: int, j: int, move: str, visited: List[List[int]]):
    if i == n-1 and j == m-1:
      res.append(move[:])
      return
    
    # Check down path
    if i+1 < n and not visited[i+1][j] and maze[i+1][j] == 1: 
      visited[i][j] = 1
      backtrack(i+1, j, move+'D', visited)
      visited[i][j] = 0
    
    # Check left path
    if j-1 >= 0 and not visited[i][j-1] and maze[i][j-1] == 1:
      visited[i][j] = 1
      backtrack(i, j-1, move+'L', visited)
      visited[i][j] = 0
    
    # Check right path
    if j+1 < m and not visited[i][j+1] and maze[i][j+1] == 1:
      visited[i][j] = 1
      backtrack(i, j+1, move+'R', visited)
      visited[i][j] = 0
    
    # Check up path
    if i-1 >= 0 and not visited and maze[i-1][j] == 1:
      visited[i][j] = 1
      backtrack(i-1, j, move+'U', visited)
      visited[i][j] = 0
      
  if maze[0][0] == 1:
    backtrack(0, 0, '', visited)
  return res
    
# n = 3
# m = 3
# visited = [[0]*m]*n
# print(visited)
maze = [
  [1,0,0,0],
  [1,1,0,1],
  [1,1,0,0],
  [0,1,1,1],
]
print(rat_in_maze(maze))