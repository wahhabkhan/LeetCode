class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Step 1: Remove all dashes and convert to uppercase
        cleaned = s.replace("-", "").upper()

        # Step 2: Build the result from the end
        result = []
        for i in range(len(cleaned)):
           # Add a dash before every k characters except the first group
           if i > 0 and (len(cleaned) - i) % k == 0:
              result.append("-")
           result.append(cleaned[i])

        return "".join(result)
        
