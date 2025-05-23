class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''.join(str (ord(ch) - ord('a') + 1) for ch in s )

        for i in range(k):
            num = str(sum(int(d) for d in num))
        
        return int(num)
