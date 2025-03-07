class Solution(object):
    def isPalindrome(self, x):
        reversed_str_x = str(x)[::-1]
        
        if reversed_str_x == str(x):
            return(True)
        else:
            return(False)
        