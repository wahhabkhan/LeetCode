class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def findAndReplacePattern(word):
            mapping = {}
            result = []
            idx = 0

            for ch in word:
                if ch not in mapping:
                    mapping[ch] = idx
                    idx += 1
                result.append(mapping[ch])

            return result

        pattern_code = findAndReplacePattern(pattern)
        
        return [word for word in words if findAndReplacePattern(word) == pattern_code]
