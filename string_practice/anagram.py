class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        s1=sorted(s1)
        s2=sorted(s2)
        if s1==s2:
            return True
        else:
            return False

s=Solution()
print(s.areAnagrams("listen", "silent"))