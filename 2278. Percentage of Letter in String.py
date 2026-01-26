class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = 0
        for ch in s:
          if ch == letter:
              count += 1

        return (count * 100) // len(s)
        
        # freq = Counter(s)
        # count = freq[letter]
        # if letter in s:
        #     percent = (count * 100) / len(s) 
        #     return percent
        # return 0

