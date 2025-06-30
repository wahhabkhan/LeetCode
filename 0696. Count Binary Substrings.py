class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_count = 0
        cur_count = 1
        result = 0

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur_count += 1
            else:
                result += min(prev_count, cur_count)
                prev_count = cur_count
                cur_count = 1
        
        result += min(prev_count, cur_count)
        return result
        
        
