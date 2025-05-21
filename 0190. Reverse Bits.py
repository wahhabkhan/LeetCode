class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
      result = 0
      for i in range(32):
        # Extract the least significant bit of n
        bit = n & 1
        # Shift result left to make room for the new bit
        result = (result << 1) | bit
        # Shift n right to process the next bit
        n >>= 1
      return result
        
