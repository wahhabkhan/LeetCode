class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        seen = set()
        freq = {char: s.count(char) for char in s}

        for char in s:
            freq[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

        
