def dp_fibonacci(n: int) -> [int]:
  # Base case
  if n == 0:
    return 0
  if n < 2:
    return 1
  
  res = [1] * (n+1)
  
  res[0] = 0
  res[1] = 1
  
  for i in range(2, n+1):
    res[i] = res[i-1] + res[i-2]
  
  return res[n]

n = 5
print(dp_fibonacci(n))