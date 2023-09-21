def fib(n: int) -> int:
  # fib(0) = 0
  if n == 0:
    return 0
  
  elif n < 2:
    return 1
  
  return fib(n-1) + fib(n-2)

n = 130
# print(fib(n))


# Dynamic solution
def dynamic_fib(n:int) -> int:
  if n == 0:
    return 0
    
  nums = [0] * (n+1)
  nums[0] = 0
  nums[1] = 1
  
  for i in range(2, n+1):
    nums[i] = nums[i-1] + nums[i-2]
  
  # print(nums)
  return nums[n]

print(dynamic_fib(n))
    
    
  
  