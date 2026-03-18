
class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        if len(s1)!=len(s2):
            return False
        dic={}
        s=set()
        
        for i in range(len(s1)):
            if s1[i] in dic:
                if dic[s1[i]] != s2[i]:
                    return False
            else:
                if s2[i] in s:
                    return False
                dic[s1[i]]=s2[i]
                s.add(s2[i])
        return True

s= Solution()
print(s.areIsomorphic("aab", "xxy"))  # True
print(s.areIsomorphic("abc", "xxz"))  # False