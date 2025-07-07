class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""

        for i in (range(len(strs[0]))):
            for string in strs:
                print(strs[0][i])
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
