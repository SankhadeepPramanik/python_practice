class Solution:
    def longestString(self, words):
        word_set = set(words)
        words.sort()  # lexicographically
        longest = ""
        
        for word in words:
            # check if all prefixes exist
            if all(word[:i] in word_set for i in range(1, len(word))):
                # update if longer or same length but lexicographically smaller
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
                    
        return longest

solution = Solution()
print(solution.longestString(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # Output: "apple"    
print(solution.longestString(["w", "wo", "wor", "worl", "world"]))  # Output: "world"