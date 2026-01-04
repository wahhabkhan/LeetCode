class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        # Case 1: strings already equal
        if s == goal:
            return len(set(s)) < len(s)

        # Case 2: strings differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) != 2:
            return False

        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
        
