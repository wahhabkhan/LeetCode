class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words = s1.split() + s2.split()

        count = Counter(words)

        return [word for word, freq in count.items() if freq == 1]
        
