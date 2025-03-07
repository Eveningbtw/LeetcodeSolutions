class Solution(object):
    def romanToInt(self, s):
        RomanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0

        for i in range(0,len(s)):
            if i + 1 < len(s) and RomanToInt[s[i]] < RomanToInt[s[i + 1]]:
                total -= RomanToInt[s[i]]
            else:
                total += RomanToInt[s[i]]
        return(total)
