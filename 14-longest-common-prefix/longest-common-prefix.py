class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        
        result = ""
        
        # Iterate over the number of characters of the first word in the array of strings
        for index in range(len(strings[0])):

            # Iterate over each individual string in the array of strings
            for string in strings:

                # If the index of the string is equal to the len of the string
                if index == len(string) or string[index] != strings[0][index]:
                    return result
            
            # Add the character at position @index of the first string in the array @strings
            result += strings[0][index]
        
        return result
