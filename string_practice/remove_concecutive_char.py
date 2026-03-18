class Solution:
    def removeConsecutiveCharacter(self, s):
        if not s:
            return ""
        s=list(s)
        l=0
        for i in range(1,len(s)):
            if s[i]!=s[l]:
                l+=1
                s[l]=s[i]
        return "".join(s[:l+1])

s=Solution()
print(s.removeConsecutiveCharacter("aaabbbcc"))  # Output: "abc"
print(s.removeConsecutiveCharacter("aabcdbcc"))    # Output: "abc"