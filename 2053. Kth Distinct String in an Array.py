class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = {}
        for word in arr:
            freq[word] = freq.get(word, 0) + 1

        distinct_count = 0
        for word in arr:
            if freq[word] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return word

        return ""
