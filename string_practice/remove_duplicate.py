class Solution:
    def removeDups(self, s):
        seen = set()
        result = ""
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result += ch
        print(seen)
        return result


s = Solution()
print(s.removeDups("gffigz"))  # Output: "gf"
print(s.removeDups("geEksforGEeks"))  