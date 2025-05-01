class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        
        result = ""
        
        for i in range(len(strings[0])):
            for string in strings:
                if i == len(string) or string[i] != strings[0][i]:
                    return result
            
            result += strings[0][i]
        
        return result
