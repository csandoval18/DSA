def minRemoveToMakeValid(s: str) -> str:
  # First pass: indentify invalid ')'
  stack = []
  s_list = list(s)
  
  for i in range(len(s_list)):
    