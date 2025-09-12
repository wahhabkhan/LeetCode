from collections import Counter
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        points = [p1, p2, p3, p4]
        dists = []
        
        # compute all 6 distances
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(dist(points[i], points[j]))
        
        count = Counter(dists)
        
        # must have 2 unique distances
        if len(count) != 2:
            return False
        
        side, diag = sorted(count.items())  # [(small, freq), (large, freq)]
        
        # check 4 sides and 2 diagonals
        return side[1] == 4 and diag[1] == 2 and side[0] > 0
