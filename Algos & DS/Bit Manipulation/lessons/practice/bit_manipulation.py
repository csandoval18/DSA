class Solution:
  def bitManipulation(self, num, i):
    ithBit = 1 if ((1 << (i-1)) & num) else 0
    setIthBit = (1 << (i-1)) | num
    clearBit = ~(1 << (i-1)) & num
    print(ithBit, setIthBit, clearBit)
  
  def bitManipulation(self, num, i):
    # Get the i'th bit using left shift (1-based indexing)
    get_bit = 1 if (num & (1 << (i - 1))) else 0
    
    # Set the i'th bit (1-based indexing)
    set_bit = num | (1 << (i - 1))
    
    # Clear the i'th bit (1-based indexing)
    clear_bit = num & ~(1 << (i - 1))
    
    # Print the results as space-separated values
    print(get_bit, set_bit, clear_bit, end="")
    
    
num = 70
i = 3
s = Solution()
s.bitManipulation(num, i)