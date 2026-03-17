class Solution:
    def getSecondLargest(self, arr):
        s=set(arr)
        if(len(s)<2):
            return -1
        largest=float('-inf')
        second_largest=float('-inf')
        for i in list(s):
            if i>largest:
                second_largest=largest
                largest=i
            if i<largest and i>second_largest:
                second_largest=i
        return second_largest
s= Solution()
print(s.getSecondLargest([1, 2,99,7,5,7,10,77,55]))
print(s.getSecondLargest([22, 22,77]))
print(s.getSecondLargest([66, 22,77]))
print(s.getSecondLargest([1, 1,1,1]))


class Solution:
    def getSecondLargest1(self, arr):
        # Code Here
        s=set(arr)
        if len(s)<2:
            return -1
        else:
            a=list(s)
            a.sort(reverse=True)
            return a[1]
s= Solution()
print(s.getSecondLargest1([1, 2,99,7,5,7,10,77,55]))
print(s.getSecondLargest1([22, 22,77]))
print(s.getSecondLargest1([66, 22,77]))
print(s.getSecondLargest1([1, 1,1,1]))