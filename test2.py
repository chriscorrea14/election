from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def _rle(self, s: str) -> str:
        output = ""
        startchar = 0
        for i in range(1, len(s)):
            if s[i] != s[startchar]:
                output += str((i - startchar)) + s[startchar]
                startchar = i
        output += str((len(s) - startchar)) + s[startchar]
        return output

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self._rle(self.countAndSay(n-1))

print(Solution().countAndSay(4))
