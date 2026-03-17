from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        s1={}
        for i in list(s):
            s1[i]=s1.get(i,0)+1
        for k,v in s1.items():
            if v==1:
                return k
        return '$'
s=Solution()
print(s.nonRepeatingChar("hello"))


from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        s1=Counter(list(s))
        print(s1)
        for k,v in s1.items():
            if v==1:
                return k
        return '$'
s=Solution()
print(s.nonRepeatingChar("hello"))