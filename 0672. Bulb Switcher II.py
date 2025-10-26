class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        # n >= 3
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8
        
