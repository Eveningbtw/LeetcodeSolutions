class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""

        # We are iterrating over every index of the array strs
        for i in (range(len(strs[0]))):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
