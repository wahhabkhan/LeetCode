class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        result = 1
        a %= MOD  # reduce a mod 1337 first

        for digit in b:
            # Each step: (previous_result^10 * a^digit) % MOD
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result
