class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = []

            for i in range(0, len(s), k):
                group = s[i:i+k]
                digit_sum = sum(int(ch) for ch in group)
                new_s.append(str(digit_sum))


            s = "".join(new_s)

        return s
