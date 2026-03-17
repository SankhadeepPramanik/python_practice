class Solution:
    def leaders(self, arr):
        # code here
        leaders_list=[]
        n=len(arr)
        for i in range(len(arr)):
            m=max(arr[i:])
            print(m, arr[i:])
            if arr[i]>=m:
                leaders_list.append(arr[i])
        return leaders_list

s= Solution()
print(s.leaders([16, 17, 4, 3, 4, 2]))
print(s.leaders([1, 8, 3, 5, 7]))

class Solution:
    def leaders(self, arr):
        n=[arr[-1]]
        max=arr[-1]
        for r in range(len(arr)-2,-1,-1):
            print(max, arr[r])
            if arr[r]>=max:
                n.append(arr[r])
                max=arr[r]
        return n[::-1]
    
s= Solution()
print(s.leaders([16, 17, 4, 3, 4, 2]))
print(s.leaders([1, 8, 3, 5, 7]))