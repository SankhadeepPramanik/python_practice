class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        
        leftProduct = 1
        rightProduct = 1
        ans = arr[0]
        
        for i in range(n):
            
            # reset if product becomes 0
            if leftProduct == 0:
                leftProduct = 1
            if rightProduct == 0:
                rightProduct = 1
            
            # prefix product (left to right)
            leftProduct *= arr[i]
            
            # suffix product (right to left)
            rightProduct *= arr[n - 1 - i]
            
            # update answer
            ans = max(ans, leftProduct, rightProduct)
        
        return ans
s= Solution()
arr = [1, -2, -3, 0, 7, -8, -2]
print(s.maxProduct(arr))  # Output: 112