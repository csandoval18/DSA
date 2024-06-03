def minRemoveToMakeValid(s: str) -> str:
  # First pass: indentify invalid ')'
  stack = []
  s_list = list(s)
  
  for i in range(len(s_list)):
    if s[i] == '(':
      stack.append(i)
    elif s[i] == ')':
      if stack:
        stack.pop()
      else:
        s_list[i] = "" # Mark for removal
    
  # Second pass (using set for faster lookup): identify invalid '(' from the end
  invalid_open_indexes = set(stack)
  for i in invalid_open_indexes:
    s_list[i] = ""
  
  # Reconstruct the valid string
  return "".join(s_list)