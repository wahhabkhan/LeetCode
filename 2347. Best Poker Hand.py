class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if all(s == suits[0] for s in suits):
            return "Flush"
        freq = {}
        for i in ranks:
            if i in freq:
                freq[i] += 1
            else: 
                freq[i] = 1 
        max_freq = max(freq.values())
        # if freq[key] == 5:
        #     return "Flush"
        if max_freq >= 3:
                return "Three of a Kind"
        if max_freq == 2:
                return "Pair"
        else:
                return "High Card"
        
