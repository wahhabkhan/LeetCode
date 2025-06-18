class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Define keyboard rows as sets for quick lookup
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            # Convert word to lowercase for case-insensitive comparison
            lower_word = set(word.lower())
        
            # Check which row all letters of the word belong to
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
               result.append(word)

        return result
        
