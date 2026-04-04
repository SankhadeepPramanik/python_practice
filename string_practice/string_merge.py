class Solution:
    def merge(self, S1, S2):
        l=""
        i=j=0
        while i < len(S1) and j < len(S2):
            l+=S1[i]+S2[j]
            i=i+1
            j=j+1
        if len(S1)>len(S2):
            l+=S1[i:]
        else:
            l+=S2[i:]
        return l
solution=Solution()
print(solution.merge("abc","defg")) 
print(solution.merge("abcd","efg"))