def removeKdigits(num: str, k: int) -> str:
  stack = []

  for char in num:
    while k > 0 and stack and stack[-1] > char:
      k -= 1
      stack.pop()
    
    stack.append(char)
  
  stack = stack[:len(stack)-k]
  res = "".join(stack)
  return res if res else "0"