class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()

        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        


        
