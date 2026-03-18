class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        s=len(pat)
        for i in range(len(txt)):
            if txt[i:i+s]==pat:
                return i
        return -1
        
s=Solution()
print(s.firstOccurence("geeksforgeeks","for"))
print(s.firstOccurence("geeksforgeeks","ior"))