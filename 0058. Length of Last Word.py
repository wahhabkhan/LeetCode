class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()
        length_last_element = len(list.pop())
        return length_last_element
