class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
    

        i = 0
        ans = 0
        while i < len(s) - 1:
            if value[s[i]] < value[s[i+1]]:
                ans += value[s[i+1]] - value[s[i]]
                i += 2 

            else:
                ans += value[s[i]]
                i += 1

        if i < len(s):
            ans += value[s[len(s)-1]]

        return ans

    





        