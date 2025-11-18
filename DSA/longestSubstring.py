class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        visited = []
        maxlen=0
        length=0
        for i in s:
            if not i in visited:
                visited.append(i)
                length+=1
            else:
                maxlen = length if maxlen<length else maxlen
                while i in visited:
                    length-=1
                    visited.pop(0)
                visited.append(i)
                length+=1
        return maxlen if length<maxlen else length
