# C++

# int findDuplicate(vector<int &arr, int n) {
#   std::sort(arr.begin(), arr.end()) 
#   int l = 0
#   int r = n-1
# 
#   while (l<=r) {
#     int m = (l+r)/2
# 
#     if (arr[m]-1 < m) {
#       r = m-1
#     } else {
#       l = m+1 
#     }
#   }
#   return arr[l]
# }

def magicIndex(a, n):
  # write your code here
  # return an integer denoting the answer
  a.sort()
  l, r = 0, n-1

  while l<=r:
    m = (l+r)//2

    if a[m]-1 < m:
      r = m-1
    else:
      l = m+1
      return 
  pass
