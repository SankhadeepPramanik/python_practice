class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        from collections import Counter
        data=Counter(list(s))
        print(data)
        sorted_items = sorted(data.items(), key=lambda item: (-item[1], item[0]))
        return sorted_items[0][0]
            
s=Solution()
print(s.getMaxOccurringChar("testsample"))  # Output: "t"