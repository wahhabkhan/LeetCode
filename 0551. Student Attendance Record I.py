class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        consecutive_L = 0
        prev = ''
        for ch in s:
            if ch == 'A':
                count_A += 1
                if count_A >=2:
                    return False           
            if ch == 'L':                        
                if prev == 'L':        
                     consecutive_L += 1        
                else:
                    consecutive_L = 1
                if consecutive_L >= 3:
                    return False
            else:
                consecutive_L = 0
            prev = ch
        return True

        # if s.count('A') >= 2:
        #     return False

        # if 'LLL' in s:
        #     return False

        # return True
      

        
                
                
