class Solution(object):
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        set1 = set(word1)
        set2 = set(word2)

        for c1 in set1:
            for c2 in set2:
                new_set1 = set1.copy()
                new_set2 = set2.copy()

                if word1.count(c1) == 1:
                    new_set1.remove(c1)

                if word2.count(c2) == 1:
                    new_set2.remove(c2)

                new_set1.add(c2)
                new_set2.add(c1)

                if len(new_set1) == len(new_set2):
                    return True
        return False
        
