#lists
def merge1(nums1, m , nums2, n):
  j = 0
  tmp = 0
  tmp2 = 0
  for i in nums1:
    if nums1[i] > nums2[j]:
      tmp = nums1[i]
      j += 1
      print(nums1[m:])
      for x in nums1[m:]:
        print("x:", x)
        if tmp < nums1[i]: 
          tmp2 = nums1[i]
          nums1[x] = tmp
  return nums1


#This one is just adding the other array's elements into the empty 0s then sorting it
def merge(nums1, m , nums2, n):
  # """
  # Do not return anything, modify nums1 in-place instead.
  # """
  cnt = 0;
  while(m < len(nums1)):
    nums1[m] = nums2[cnt];
    cnt+=1
    m+=1
  nums1.sort();
  return nums1
  
# *len(nums1) = m+n
def merge(nums1, m, nums2, n):
  index = m+n-1
  while(n>0):
    if(m>0 and nums1[m-1]>nums2[n-1]):
      nums1[index] = nums1[m-1];
      m-=1;
    
    else:
      nums1[index] = nums2[n-1];
      n-=1;
    
    index -=1;

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(merge(nums1, 3, nums2, 3))