Prefix Sum Concept
What is a Prefix Sum?

A prefix sum array is an auxiliary array that stores the cumulative sums of the elements of the original array up to each index.

Why use Prefix Sum?

To quickly calculate the sum of any subarray in constant time O(1) after a linear preprocessing step.

Avoid repeated summations during queries.

How does it work?

Given an array arr of length n:

Create a prefix sum array prefix where:
𝑝𝑟𝑒𝑓𝑖𝑥[𝑖]=𝑎𝑟𝑟[0]+𝑎𝑟𝑟[1]+⋯+𝑎𝑟𝑟[𝑖]
prefix[i]=arr[0]+arr[1]+⋯+arr[i]

To find the sum of subarray arr[i...j], use:

sum(i, j) = prefix[j] - prefix[i-1]   if i > 0
sum(i, j) = prefix[j]                  if i == 0

sum(i,j)=prefix[j]−prefix[i−1](if i>0)

Otherwise, if i == 0, sum is just prefix[j].

Step-by-step example:
arr = [2, 4, 6, 8, 10]


Compute prefix sums:

Index (i)	0	1	2	3	4
arr[i]	    2	4	6	8	10
prefix[i]	2	6	12	20	30

(Explanation: prefix[1] = 2 + 4 = 6, prefix[2] = 6 + 6 = 12, etc.)

To find the sum of subarray arr[1..3] (4 + 6 + 8):

𝑠𝑢𝑚=𝑝𝑟𝑒𝑓𝑖𝑥[3]−𝑝𝑟𝑒𝑓𝑖𝑥[0]=20−2=18
sum=prefix[3]−prefix[0]=20−2=18

arr = [2, 4, 6, 8, 10]

# Build prefix sum array
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

# Query sum of subarray arr[left..right]
left, right = 1, 3
sub_sum = prefix[right] - (prefix[left-1] if left > 0 else 0)

print(sub_sum)  # Output: 18


Time Complexity:

Building prefix sum array: O(n)

Each subarray sum query: O(1)

Common Uses:

Range sum queries

Quickly calculating sums in sliding window problems

Finding sums with constraints

Useful in many algorithm problems to speed up calculations
count of subarray with sum k
arr = [1, 2, 3, 0, 3]
k = 3

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

print(result)  # Output: 4

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
