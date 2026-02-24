class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        groups = 1

        for i in range(1, len(word)):
            if word[i] <= word[i-1]:
                groups +=1
            
        return groups * 3 - len(word)
        
