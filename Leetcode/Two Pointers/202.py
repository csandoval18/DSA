# Happy number = starting with a + int
def isHappy(n: int) -> bool:
  seen = set()
  
  while n != 1 and n not in seen:
    seen.add(n)
    res = 0
    while n > 0:
      digit = n%10
      n //= 10
      res += digit ** 2
    n = res
  return n == 1

n = 2
print(isHappy(n))
print(234%10)
print(234//10)