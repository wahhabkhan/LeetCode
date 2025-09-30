class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # for i in range(1, int(num ** 0.5) +1):
        #     if i * i == num:
        #         return True 
        # return False

        #Binary Search
        if num < 2:
            return True
        low, high = 2, num // 2

        while low <= high:
            mid = (low + high) // 2     
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1            
            else:
                high = mid - 1           
        return False
