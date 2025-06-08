class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for sc, tc in zip(s, t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                if tc in t_to_s:
                    return False
                s_to_t[sc] = tc
                t_to_s[tc] = sc

        return True
