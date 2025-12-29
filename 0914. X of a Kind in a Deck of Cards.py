class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)

        g = 0
        for count in freq.values():
            g = gcd(g,count)
        
        return g>1
