def fibonacci(n: int) -> int:
  if n == 0:
    return 1
  if n == 1:
    return 1
  
  fib = fibonacci(n-1) + fibonacci(n-2)
  return fib

n = 5
print(fibonacci(n))