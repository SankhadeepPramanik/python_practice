class Solution:
    def subarraySum(self, arr, k):
        """
        Count the number of subarrays with sum equal to k.
        :param arr: List[int] - input array
        :param k: int - target sum
        :return: int - number of subarrays summing to k
        """
        count_map = {0: 1}  # Prefix sum 0 occurs once
        current_sum = 0
        result = 0

        for num in arr:
            current_sum += num

            # Check if there's a prefix sum that makes subarray sum = k
            if (current_sum - k) in count_map:
                result += count_map[current_sum - k]

            # Update the map
            count_map[current_sum] = count_map.get(current_sum, 0) + 1

        return result


# Example usage
arr = [3, 1, 1, 2, 1]
k = 2
sol = Solution()
print(sol.subarraySum(arr, k))  # Output: 4