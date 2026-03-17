class Solution:
    def missingNum(self, arr):
        s = set(arr)
        for i in range(1, len(arr) + 2):
            if i not in s:
                return i
s = Solution()
print(s.missingNum([1, 2, 3, 5]))