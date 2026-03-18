class Solution:
    def isRotated(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return False
        sl=s1[2:]+s1[:2]
        sr=s1[-2:] + s1[:-2]
        if s2==sl or s2==sr:
            return True
        else:
            return False
        
s= Solution()   
print(s.isRotated("amazon","azonam"))
print(s.isRotated("amazon","aoonma"))