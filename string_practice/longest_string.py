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

solution = Solution()
print(solution.longestString(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # Output: "apple"    
print(solution.longestString(["w", "wo", "wor", "worl", "world"]))  # Output: "world"
print(solution.longestString(["a", "bo", "bcu"]))  # Output: "a" (or "b" or "c")