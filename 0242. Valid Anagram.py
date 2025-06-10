class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0 ) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0 ) + 1
        
        return count_s == count_t
