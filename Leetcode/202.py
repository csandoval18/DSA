def isHappy(n):
  while n >= 1:
    if n == 1:
      return True
      
    # Turn number into array of digits
    num = n
    arr = []
    while num != 0:
      arr = [num % 10] + arr
      num = num // 10
    print(arr)
      
    total = 0
    for i in arr:
      total += i ** 2
    print(n)
    if total == n:
      return False
    n = total
    
n = 2
print(isHappy(n))