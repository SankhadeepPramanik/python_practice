#sliding window technique to find the maximum sum of a subarray of size k
def max_sum_subarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None  # or raise ValueError("Invalid input")
    # window_sum = 0
    # # Build the first window
    # for i in range(k):
    #     window_sum += arr[i]
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

result=max_sum_subarray([1, 2, 3, 4, 5], 2)
print(result)  # Output: 9 (subarray [4, 5] has the maximum sum of 9)