#sliding window technique to find the longest substring with at most k distinct characters
class Solution:
    def longestKSubstr(self, s, k):
        if k == 0:
            return -1

        left = 0
        longest = -1
        char_count = {}

        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1

            if len(char_count) == k:
                longest = max(longest, right - left + 1)

        return longest
    

solution = Solution()
result = solution.longestKSubstr("abbcba", 2)
print(result) # Output: 4 (the longest substring with at most 2 distinct characters is "bbcb")