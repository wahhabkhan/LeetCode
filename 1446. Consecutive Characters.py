class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 1
        count = 1
        ch = s[0]
        for i in range(1,len(s)):
            if s[i] == ch:
                count += 1
                max_count = max(max_count, count)
            else:
                ch = s[i]
                count = 1
        return max_count            
