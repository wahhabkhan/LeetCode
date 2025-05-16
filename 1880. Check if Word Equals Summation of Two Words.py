class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def word_to_num(word):
          return int(''.join(str(ord(c) - ord('a')) for c in word))

        return word_to_num(firstWord) + word_to_num(secondWord) == word_to_num  (targetWord)
         

        
        
