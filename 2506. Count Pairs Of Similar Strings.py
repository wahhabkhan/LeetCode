class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        freq = {}
        pairs = 0

        for word in words:
            key = frozenset(word)
            freq[key] = freq.get(key,0) + 1

        for count in freq.values():
            pairs += count * (count - 1) //2

        return pairs 
        
