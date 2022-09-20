class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+l]==needle:
                    return i
        return -1
