class Solution:
    
    str1=""
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            str1=s.replace(s[i],"",1)
            if str1==str1[::-1]:
                return True
        
        return False
