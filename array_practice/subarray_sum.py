
#sliding window technique to find the first subarray that sums to a target value
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
                return [left + 1, right + 1]  # 1-based index

        return [-1]
solution = Solution()
result = solution.subarraySum([10, 20, 3, 4, 5], 23)
print(result)  # Output: [4, 5] (subarray [4, 5] has the sum of 9)