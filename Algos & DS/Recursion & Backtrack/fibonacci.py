def fib(n: int) -> int:
  # fib(0) = 0
  if n == 0:
    return 0
  
  elif n < 2:
    return 1
  
  return fib(n-1) + fib(n-2)

n = 130
# print(fib(n))