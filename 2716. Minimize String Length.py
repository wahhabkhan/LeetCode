class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return len(set(s))
        seen = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            seen[idx] = 1

        count = 0
        for val in seen:
            count += val

        return count


        
