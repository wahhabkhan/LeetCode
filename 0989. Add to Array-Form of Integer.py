class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        #word = '0'
        # for element in num:
        #     word += str(element)
        
        word = ''.join(str(x) for x in num)

        word = k + int(word)

        return [int(digit) for digit in str(word)]
        
        
