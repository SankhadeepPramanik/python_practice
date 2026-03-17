class Solution:
    def findDuplicates(self, arr):
        seen = set()
        d = set()
        for x in arr:
            if x in seen:
                d.add(x)
            else:
                seen.add(x)

        return list(d)

s= Solution()
print(s.findDuplicates([1, 2,7,6,7,4,1]))