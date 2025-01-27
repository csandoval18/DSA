class Solution:
  def bitManipulationAttempt(self, num, i):
    ithBit = (1 << i)
    setIthBit = (1 << i) & num
    clearBit = ~(1 << i) & num
    return ithBit, setIthBit, clearBit
    
  def bitManipulation(self, num, i):
    # Get the i'th bit using left shift (1-based indexing)
    get_bit = 1 if (num & (1 << (i - 1))) else 0
    
    # Set the i'th bit (1-based indexing)
    set_bit = num | (1 << (i - 1))
    
    # Clear the i'th bit (1-based indexing)
    clear_bit = num & ~(1 << (i - 1))
    
    # Print the results as space-separated values
    print(get_bit, set_bit, clear_bit, end="")