def moveZeroesToLeft(arr, n):
  a, b = n-1, n-1
  #a = r, b = l
  
  while b >= 0:
    if arr[b] != 0:
      arr[a], arr[b] = arr[b], arr[a]
      a -= 1
    b -= 1
  return arr
  
def sortedBinaryArr(arr, n):
  l, r = 0, 0
  
  while l<n:
    if arr[l] != 1:
      arr[l], arr[r] = arr[r], arr[l]
      r += 1
    l += 1
  return arr
      
def sortedBinaryArr(arr, n):
  l, r = 0, 0
  
  while l<n:
    if arr[l] == 0:
      arr[l], arr[r] = arr[r], arr[l]
      r += 1
    l += 1
  return arr
#          a
# [1,2,0,0,1]
#          b

# swap, a--, b--
#        a 
# [1,2,0,0,1]
#        b 

# b--
#        a 
# [1,2,0,0,1]
#      b   

# b--
#        a 
# [1,2,0,0,1]
#    b

# swap, a--, b--
#      a   
# [1,0,0,2,1]
#  b   

# swap, a--, b--
#      a   
# [0,0,1,2,1]
#  b   

#         a   
#    [0,0,1,2,1]
#  b   
# b < 0
# End of iteration

# -----------------------------------------------------------------

#                a
# [2,2,2,0,0,5,5,0]
#                b

# b--
#                a
# [2,2,2,0,0,5,5,0]
#              b

# swap, b--, a--
#              a
# [2,2,2,0,0,5,0,5]
#            b

# swap, b--, a--
#            a 
# [2,2,2,0,0,0,5,5]
#          b

# b--
#            a 
# [2,2,2,0,0,0,5,5]
#        b

# b--
#            a 
# [2,2,2,0,0,0,5,5]
#      b

# swap, b--, a--
#          a 
# [2,2,0,0,0,2,5,5]
#    b

# swap, b--, a--
#          a 
# [2,2,0,0,0,2,5,5]
#    b

# swap, b--, a--
#        a 
# [2,0,0,0,2,2,5,5]
#  b

# swap, b--, a--
#        a 
# [0,0,0,2,2,2,5,5]
#  b