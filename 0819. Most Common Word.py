class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(banned)

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.lower().split()
        counts = Counter(w for w in words if w not in banned_set)

        return max(counts, key=counts.get)


        
