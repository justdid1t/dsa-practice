class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = []
        if len(s) == 0:
            ans = [0]
        else:
            ans = [1]
        i = 0
        length = len(s)
        
        
        while i < length:
            j = i
            substr = []
            
            while j < length:
                if s[j] in substr:
                    ans.append(len(substr))
                    break
                else:
                    substr.append(s[j])
                    j += 1
                    if j == length:
                        ans.append(len(substr))
                    
            i += 1
            
        
        return max(ans)
        


s = input()
ans = Solution()  #object
print(ans.lengthOfLongestSubstring(s))



                    
                    
                    
                
                
                