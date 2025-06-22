class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_set = set()
        upper_set = set()

        for char in word:
            if char.islower():
                lower_set.add(char)
            else:
                upper_set.add(char.lower())
        
        return len(upper_set & lower_set)
        
