# Kadane’s Algorithm is used to find the maximum sum of a contiguous subarray.

# I’ll explain it very simply, step by step, with an example.

# Problem Statement

# Given an array of integers (can include negative numbers), find the maximum sum of any continuous subarray.

# Example
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Answer: 6
# (subarray = [4, -1, 2, 1])

# Main Idea (Very Important)

# At each position:

# Either start a new subarray

# Or continue the previous subarray

# We always keep the best sum so far.

class Solution:
    def maxSubArraySum(self, arr):
        current_sum = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


# Dry Run (Easy to Understand)
# Array:
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i	arr[i]	current_sum	max_sum
0	-2	        -2	    -2
1	1	max(1, -2+1)=1	1
2	-3	max(-3, 1-3)= -2 1
3	4	max(4, -2+4)=4	4
4	-1	max(-1, 4-1)=3	4
5	2	max(2, 3+2)=5	5
6	1	max(1, 5+1)=6	6
7	-5	max(-5, 6-5)=1	6
8	4	max(4, 1+4)=5	6
Final Answer
Maximum Subarray Sum = 6


Kadane’s Algorithm – Core Idea

At every element, we decide:

👉 Extend the previous subarray
OR
👉 Start a new subarray

This decision is made using current_sum.

Meaning of Variables

current_sum
→ Maximum subarray sum ending at the current index

max_sum
→ Maximum subarray sum found so far

The Key Line (Heart of Kadane)
current_sum = max(arr[i], current_sum + arr[i])


This single line handles all 4 scenarios in the image.

Understanding the 4 Scenarios
🟢 Scenario 1

Previous subarray sum: +ve
Current element: +ve

(+ve) + (+ve) = better


✅ Extend subarray

Example:

current_sum = 5
arr[i] = 3
→ extend → 8

🔴 Scenario 2

Previous subarray sum: -ve
Current element: +ve

(-ve) + (+ve) < (+ve)


✅ Start new subarray

Example:

current_sum = -4
arr[i] = 6
→ new start → 6

🟢 Scenario 3

Previous subarray sum: +ve
Current element: -ve

(+ve) + (-ve) may still help


✅ Extend subarray

Example:

current_sum = 10
arr[i] = -3
→ extend → 7

🔴 Scenario 4

Previous subarray sum: -ve
Current element: -ve

(-ve) + (-ve) is worse


✅ Start new subarray

Example:

current_sum = -5
arr[i] = -2
→ new start → -2






Backtracking:
    
class Solution:
    def findPermutation(self, nums):
        result = set()  # to avoid duplicates

        def backtrack(current, remaining):
            if not remaining:
                result.add(tuple(current))  # convert list to tuple for set
                return
            for i in range(len(remaining)):
                backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return [list(p) for p in result]  # convert tuples back to lists

# Examples:
sol = Solution()
print(sol.findPermutation([1, 2, 3]))  # all 6 permutations
print(sol.findPermutation([1, 1]))     # only [[1,1]]
print(sol.findPermutation([1, 1, 2]))  # [[1,1,2], [1,2,1], [2,1,1]]


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

