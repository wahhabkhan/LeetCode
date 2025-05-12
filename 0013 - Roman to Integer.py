class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
    
        for char in reversed(s):
          current = roman_map[char]
          if current < prev_value:
            total -= current
          else:
            total += current
          prev_value = current

        return total  
