# (1 based indexing)

class Solution:
  def bitManipulation(self, num, i):
    ithBit = 1 if ((1 << (i-1))) else 0
    setIthBit = 1 | (1 << i) & num
    clearBit = ~(i << i) & num
        
    return  ithBit, setIthBit, clearBit

num = 70
i = 3
s = Solution()
print(bin(70))
print(s.bitManipulation(num, i))