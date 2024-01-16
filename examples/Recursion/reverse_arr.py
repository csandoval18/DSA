def reverse(i: int, arr: [int], n: int) -> int:
  if i >= n/2: 
    return
  
  arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
  reverse(i+1, arr, n)
  
  return arr

arr = [1,2,3,4]
print(reverse(0, arr, len(arr)))


# n = 3
# for i in range(n):
#   for j in range(n-i-1):
#     print("*", end=" ")
#   print()