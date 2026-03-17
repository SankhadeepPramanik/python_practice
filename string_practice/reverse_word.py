class Solution:
    def reverseWords(self, s):
        # code here
        s1=[ w for w in s.split(".") if w][::-1]
        s2='.'.join(s1)
        return s2
    
s=Solution()    
print(s.reverseWords("i.like.this.program.very.much"))

class Solution1:
    def reverseWords(self, s):
        # code here'list
        l=[]
        for i in s.split("."):
            l.append(''.join(list(i)[::-1]))
            print(l)
            
        return '.'.join(l[::-1])
    
s=Solution1()    
print(s.reverseWords("i.like.this.program.very.much"))