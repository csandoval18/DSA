# Not using slicing O(n^3)
def iterateSubarrays1(arr):
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      subarray = []
      print("i:", i)
      print("j:", j)
      # Range for k range(i, j+1) => the +1 is needed to make the j value inclusive in the range
      for k in range(i, j+1):
        print("k:", k)
        subarray.append(arr[k])
      print(subarray)
      print("\n")
      
      
# Using python slicing, otherwise it uses an extra loop
def iterate_subarrays(arr):
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      subarray = arr[i:j+1]
      print(subarray)
      

def iterateSubarrays(arr):
  n = len(arr)
  
  for i in range(n):
    
    for j in range(i, n):
      subarray = []
      
      for k in range(i, j+1):
        subarray.append(arr[k])
        
      print(subarray)
      

arr = [1,2,3,4]
# iterate_subarrays(arr)
iterateSubarrays1(arr)
