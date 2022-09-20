class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0,len(s)-1,2):
            if s[i]==s[i+1]:
                return "true"
        return "false"
