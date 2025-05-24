class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        freq = [0] * 10

        for ch in num:
            freq[int(ch)] += 1

        for i in range(len(num)):
            if int(num[i]) != freq[i]:
                return False

        return True
                    
