class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = {}
        for ch in magazine:
            char_count[ch] = char_count.get(ch,0) + 1
        
        for ch in ransomNote:
            if char_count.get(ch,0) == 0:
                return False
            char_count[ch] -= 1

        return True
        
