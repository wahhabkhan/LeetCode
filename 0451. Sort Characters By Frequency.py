class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        sorted_chars = sorted(freq.keys(), key=lambda x:freq[x], reverse=True)

        result = []
        for ch in sorted_chars:
            result.append(ch * freq[ch])

        return "".join(result)

        
