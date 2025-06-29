class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(i, j):
            while i<j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1
            return True                    

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)

            left += 1
            right -= 1

        return True 
        
