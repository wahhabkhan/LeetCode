class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)

        words_sorted = sorted(freq.keys(), key=lambda w:(-freq[w], w))

        return words_sorted[:k]
