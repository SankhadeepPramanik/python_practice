														Two Pointer
											----------------------------------------
What is the Two Pointer Technique?

Using two indices (pointers) to traverse a data structure (usually an array or string) instead of nested loops.

WHY use Two Pointers?

Avoid O(n²) brute-force solutions

Reduce time complexity to O(n) or O(n log n)

Cleaner, more efficient logic

WHEN to use Two Pointers?
1️⃣ Array or String problems
----------------------------
Especially when:

The data is sorted

You are searching for pairs, subarrays, or conditions

2️⃣ Need to compare or shrink a range
-----------------------------------
Palindromes

Subarrays / substrings

Removing duplicates

3️⃣ Problems that say:
----------------------------
“Find pair…”

“Longest / shortest subarray”

“At most / at least K”

“Without repeating characters”

HOW to use Two Pointers (Patterns)
Pattern 1: Opposite Direction Pointers


Example: Two Sum (Sorted Array)
------------------------------------------------
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return []
    
--------------------------------------------------------------------------------------------------
different two pointer:
------------------------------------------------------------------------------------------------
1. Converging Pointers
-------------------------
What is it?

Two pointers start at opposite ends of the array or string and move towards each other until they meet or cross.

When to use?

Problems involving pairs or symmetrical checks

Palindromes, reverse operations

Pair sums in sorted arrays

How it works?

left starts at 0

right starts at the last index

Move left forward or right backward based on conditions

Stop when left >= right

Example: Check if string is a palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

2. Parallel Pointers
------------------------------
What is it?

Two pointers that move in the same direction through the array/string but at different speeds or with different conditions.

When to use?

Removing duplicates
All Zero do right
Partitioning arrays

Copying/modifying arrays in place

How it works?

slow pointer tracks position of last unique/valid element

fast pointer explores new elements ahead

When condition met, update slow and move both pointers forward

Example: Remove duplicates in sorted array
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
ABBCDD

def zero_right(arr:list)->list:
    left=0
    for r in range(1,len(arr)):
        if arr[r]!=0:
            arr[left],arr[r]=arr[r],arr[left]
            left+=1
    return arr

a=zero_right([0,0,1,0,2,3,0,9,6,7,0])
print(a)

3. Trigger-Based Pointers
-------------------------------------
What is it?

One pointer moves forward triggering conditions to move the other pointer. Often seen in sliding window or dynamic window problems.

When to use?

Problems with variable-size windows

Constraints based on sum, frequency, count, or other conditions

Longest/shortest substring or subarray with conditions

How it works?

right pointer expands the window, adding elements

When a condition is violated, left pointer shrinks the window until valid

Update result during expansion or shrinking

Example: Longest substring with no repeating characters
def length_of_longest_substring(s):
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

Summary Table
Pointer Type	Pointer Movement	Use Cases	Example
Converging Pointers	Two pointers start at ends, move inward	Palindromes, pair sums	Palindrome check
Parallel Pointers	Both move forward, one fast, one slow	Remove duplicates, partition	Remove duplicates in sorted array
Trigger-Based	One expands window, other shrinks on trigger	Sliding window, variable size	Longest substring no repeats