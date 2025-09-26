class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        dic = defaultdict(int)   # auto initializes with 0
        #dic = {}
        for i in range(lowLimit, highLimit + 1):
            sum_digit = 0
            for dig in str(i):
                sum_digit += int(dig)
                
            # if sum_digit not in dic:
            #     dic[sum_digit] = 0

            dic[sum_digit] += 1

        return max(dic.values())  
                

                            
        
