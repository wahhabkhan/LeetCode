class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        count = []

        for ch in s:
            if res and res[-1] == ch:
                count[-1] += 1
                res.append(ch)
                if count[-1] == k:
                    for i in range(k):
                        res.pop()
                    count.pop()
            else:
                res.append(ch)
                count.append(1)

        return "".join(res)
                
