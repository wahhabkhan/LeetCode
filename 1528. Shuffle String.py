class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ""  
        for i in range(len(indices)): 
            ans += s[indices.index(i)] # firstly we`ll get the index of "i", and then we use that to have the char in the string. I.E. indices.index(0) = 4 ,s[4] = L
        return ans 
        
