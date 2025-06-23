class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = set(s)
        for ch in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if ch in letters and ch.lower() in letters:
                return ch

        return ""
        
