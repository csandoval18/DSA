# Backtracking solution
def maxLengthBacktrack(arr):
  def is_unique(s):
    return len(s) == len(set(s))

  def backtrack(index, current_str):
      nonlocal max_length

      if is_unique(current_str):
        max_length = max(max_length, len(current_str))

      for i in range(index, len(arr)):
        backtrack(i + 1, current_str + arr[i])
        
  max_length = 0
  max_length = backtrack(0, "")
  return max_length

# Recursive solution
def maxLength(arr):
  def is_unique(s):
      return len(s) == len(set(s))

  def recursive(index: int = 0, current_str:str = ""):
    if index == len(arr):
      return len(current_str) if is_unique(current_str) else 0

    # Exclude the current string
    without_current = recursive(index + 1, current_str)
    
    # Include the current string if it has unique characters
    if is_unique(current_str + arr[index]):
        with_current = recursive(index + 1, current_str + arr[index])
    else:
        with_current = 0

    return max(without_current, with_current)

  return recursive(0, "")


# Example usage:
arr = ["un", "iq", "ue"]
result = maxLength(arr)
print(result)
