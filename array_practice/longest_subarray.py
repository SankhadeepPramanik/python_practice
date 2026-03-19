class Solution:
    def longestSubarray(self, arr, k):
        seen = {}  # first occurrence of each prefix sum
        current_sum = 0
        max_len = 0

        for i, num in enumerate(arr):
            current_sum += num

            # subarray from index 0 to i
            if current_sum == k:
                max_len = i + 1

            # subarray from some previous index to i
            if (current_sum - k) in seen:
                max_len = max(max_len, i - seen[current_sum - k])

            # store first occurrence of current_sum
            if current_sum not in seen:
                seen[current_sum] = i

        return max_len
    
solution = Solution()
print(solution.longestSubarray([1, -1, 5, -2, 3], 3))  # Output: 4
print(solution.longestSubarray([-2, -1, 2, 1], 1))  # Output: 2