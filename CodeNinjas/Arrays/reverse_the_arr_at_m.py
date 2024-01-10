# Given arr reverse the arr slice at index m (non inclusive)

# Ex:
# arr = [1,2,3,4,5,6]
# n = 6
# m = 3
# out: arr = [1,2,3,4,6,5]

def reverseArray(arr, m):
  res = arr[:m+1] + arr[m+1:][::-1]
  return res


arr = [1,2,3,4,5,6]
n = len(arr)
m = 3

print(arr[:m+1])
# [1,2,3,4]
print(arr[m+1:])
# [5,6]
print(reverseArray(arr, m))
# [1,2,3,4,6,5]

# Python slicing

# End slicing is inclusive at index
# arr = [1,2,3,4,5,6]
# arr[:3] = [1,2,3,4]
#            0 1 2 3

# Start slicing is non inclusive at index
# arr = [1,2,3,4,5,6]
#        0 1 2 3 4 5
# Notice how index 3 is not included
# arr[3:] = [5,6]