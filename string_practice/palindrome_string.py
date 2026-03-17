class Solution:
    def isPalindrome(self, s):
        # code here
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
    
s=Solution()
print(s.isPalindrome("madam"))