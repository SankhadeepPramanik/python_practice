													sliding window:(l -----> r -----> r -----> r)
                                               -------------------------
What Is Sliding Window?

It’s a two-pointer technique where a window (subarray / substring) expands and shrinks while moving through the array once.
✅ When SHOULD You Use Sliding Window?
Array / String is CONTIGUOUS

You are dealing with:

Subarray

Substring

Continuous segment

❌ Not for subsequence
❌ Not for picking random elements
------------------------------------------------------------------------------------------------------
fixed window:
--------------------------------------------------------------------------------------------------------
initialize window_sum = 0
initialize max_result (or other required value)

# Set up the initial window
for i from 0 to k - 1:
    window_sum += arr[i]

max_result = window_sum   # Initialize result

# Slide the window across the array
for i from k to arr.length - 1:
    window_sum += arr[i]-arr[i - k]     # add new element   # remove old element

    update max_result (or other computation)

return max_result (or other required value)

example:
Find the maximum sum of a subarray of size k
-----------------------------------------------------
def max_sum_subarray(arr, k):
    window_sum = 0

    # Build the first window
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i]        # add next element
        window_sum -= arr[i - k]    # remove element leaving window
        max_sum = max(max_sum, window_sum)

    return max_sum
---------------------------------------------------------------------------------------------------------------------
dynamic window:
---------------------------------------------------------------------------------------------------------------------
initialize left = 0
initialize window_state (sum, count, frequency map, etc.)
initialize min_or_max_result

for right from 0 to arr.length - 1:
    update window_state to include arr[right]   # Expand the window

    while window_state violates the condition:
        update min_or_max_result (if needed)
        update window_state to exclude arr[left]  # Shrink the window
        move left pointer forward

return min_or_max_result

Sliding Window Works

Because:

Subarray = continuous

All numbers are positive

Key rule:

If sum is too small → expand window (move r)

If sum is too large → shrink window (move l)

This works only because values are positive
ex:
-----------------------------------
    “Subarray with given sum”
    -----------------------------
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        curr_sum = 0
        left = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                # GFG expects 1-based indexing
                return [left + 1, right + 1]
        
        return [-1]

--------------------------------------------------
Longest Substring Without Repeating Characters (Python)
--------------------------------------------------------------
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
    
ABCABCAD
AXXRS

class Solution:
    def longestKSubstr(self, s, k):
        # code here
        left = 0
        longest = -1
        char_count = {}  # counts of characters in current window
    
        for right in range(len(s)):
            # add current character to dictionary
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
    
            # shrink window if unique characters > k
            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
    
            # update longest if exactly k unique characters
            if len(char_count) == k:
                longest = max(longest, right - left + 1)
    
        return longest
        
class Solution():
    def longestString(self, words):
        # code here
        word_set = set(words)
        words.sort()  # sort lexicographically
        longest = ""
    
        for word in words:
            # check if all prefixes of word are in the set
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                # choose longest, or lexicographically smallest if tie
                if len(word) > len(longest):
                    longest = word
    
        return longest
        

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        n, m = len(S1), len(S2)
        dp = [[0] * (m+ 1) for _ in range(n + 1)]
        ans = 0
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
    
        return ans
        
class Solution:
    def countSubstr(self, s, k):
        # Helper function: count substrings with at most k distinct chars
        def atMostK(s, k):
            from collections import defaultdict
            count = defaultdict(int)
            l = 0
            res = 0
            
            for r in range(len(s)):
                count[s[r]] += 1
                
                while len(count) > k:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        del count[s[l]]
                    l += 1
                
                # All substrings ending at r with at most k distinct chars
                res += r - l + 1
            return res
        
        # Exactly k distinct = atMostK(k) - atMostK(k-1)
        return atMostK(s, k) - atMostK(s, k-1)


class Solution:
    def longestKSubstr(self, s, k):
        # code here
        left = 0
        longest = -1
        char_count = {}  # counts of characters in current window
    
        for right in range(len(s)):
            # add current character to dictionary
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
    
            # shrink window if unique characters > k
            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
    
            # update longest if exactly k unique characters
            if len(char_count) == k:
                longest = max(longest, right - left + 1)
    
        return longest
        
        
class Solution:
    def findPermutation(self, s):
        result = set()  # use a set to avoid duplicates

        def generate(current, remaining):
            if not remaining:
                result.add(current)  # add to set
                return
            for i in range(len(remaining)):
                generate(current + remaining[i], remaining[:i] + remaining[i+1:])

        generate("", s)
        return list(result)  # convert set to list at the end


data_dict = {'apple': 3, 'banana': 2, 'cherry': 3, 'date': 1}

# Sort the items (key-value pairs)
# The key for sorting is a tuple: (-item[1], item[0])
# item[1] is the value. Negating it sorts values in descending order for numbers.
# item[0] is the key, which acts as a tie-breaker in ascending order.
sorted_items = sorted(data_dict.items(), key=lambda item: (-item[1], item[0]))

# The first element of the sorted list is the desired (key, value) pair.
# We take the first element [0] and then the key [0] from that pair.
first_key = sorted_items[0][0]

print(f"Original dictionary: {data_dict}")
print(f"The first key after sorting is: {first_key}")
