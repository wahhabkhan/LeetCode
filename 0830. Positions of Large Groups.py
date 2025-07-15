class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        res = []
        i = 0  # Start of the group
        for j in range(len(s)):
            # If it's the last character or current char ≠ next char
            if j == len(s) - 1 or s[j] != s[j + 1]:
                if j - i + 1 >= 3:
                    res.append([i, j])
                i = j + 1  # Move to next group
        return res
