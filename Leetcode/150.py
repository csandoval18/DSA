from typing import List

# BF O(n^2)
def evalRPNBF(temperatures: List[int]) -> List[int]:
  n = len(temperatures)
  res = []
  
  for i in range(n):
    for j in range(i, n):
      if temperatures[i] < temperatures[j]:
        res.append(j-i)
        break
      if j == n-1:
        res.append(0)
  return res
        
        
def evalRPN(temperatures: List[int]) -> List[int]:
  n = len(temperatures)
  res = [0]*n
  st = []
  
  for i in range(n):
    print(st)
    while st and temperatures[i] > temperatures[st[-1]]:
      print("running")
      prev_idx = st.pop()
      res[prev_idx] = i-prev_idx
      
    st.append(i) 
  return res

# st = []
# res = [0,0,0,0,0,0,0,0]

# i = 0 
# st.append(0)
# st = [0]

# i = 1
# temperatures[i] > temperatures[st[len(st)-1]]
# 74 > 73 = T
# prev_idx = st.pop() => 0
# res[prev_idx] = i-prev_idx => [1,0,0,0,0,0,0,0]

# st.append(1)
# st = [1]

# i = 2
# 75 > 74
# prev_idx = st.pop() => 1
# res = [1,1,0,0,0,0,0,0]
# st.append(2)
# st= [2]

# i = 3
# 71 > 75 = False
# st.append(3)
# st = [2,3]









temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
print(evalRPN(temperatures))