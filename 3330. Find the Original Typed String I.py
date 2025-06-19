class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        groups = []
        i = 0

        while i < n:
           j = i
           while j < n and word[j] == word[i]:
               j += 1
           groups.append(j - i)
           i = j

        total = 1  # original string (no mistake)
        for count in groups:
           total += count - 1  # reduce each group only once

        return total                   
        
