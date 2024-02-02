def sum_of_subarray_minimums(arr):
  MOD = 10**9 + 7
  stack = []
  result = 0
  arr.append(0)  # Add a sentinel element to handle the remaining elements in the stack at the end.

  for i, num in enumerate(arr):
    while stack and arr[stack[-1]] > num:
      j = stack.pop()
      k = stack[-1] if stack else -1
      result += arr[j] * (i - j) * (j - k)

    stack.append(i)

  return result % MOD