class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=right=0
        res=0
        dic={}
        while right<len(s):
            if s[right] in dic and left<=dic[s[right]]:
                left=dic[s[right]]+1
            res=max(res,right-left+1)
            dic[s[right]]=right
            right+=1
        return res