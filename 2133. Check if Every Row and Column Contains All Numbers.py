class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        required = set(range(1, n+1))

        for row in matrix:
            if set(row) != required:
                return False
        
        for col in zip(*matrix):
            if set(col) != required:
                return False

        return True
