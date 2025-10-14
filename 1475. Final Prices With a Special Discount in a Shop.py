class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        res = []

        for i in range(n):
            discount = 0
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            res.append(prices[i] - discount)

        return res 
        
