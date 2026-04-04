class Solution:
    def binarysearch(self, arr, k):
        beg = 0
        end = len(arr) - 1
        ans = -1
        
        while beg <= end:
            mid = (beg + end) // 2
            
            if arr[mid] == k:
                ans = mid          # store answer
                end = mid - 1      # move left
            elif k > arr[mid]:
                beg = mid + 1
            else:
                end = mid - 1
                
        return ans
s = Solution()
print(s.binarysearch([1, 1,1,2, 2, 3, 4], 2))
print(s.binarysearch([1, 2, 3, 4, 5], 6))