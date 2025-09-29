class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_freq = {}
        color_freq = {}
        result = []

        for ball, color in queries:
            if ball in ball_freq:
                old = ball_freq[ball]
                color_freq[old] -= 1
                if color_freq[old] == 0:
                    del color_freq[old]

            ball_freq[ball] = color
            color_freq[color] = color_freq.get(color,0) + 1
            result.append(len(color_freq))

        return result 
