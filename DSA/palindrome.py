def isPalindrome( s: str) -> bool:
        s=''.join(x.lower() for x in s if x.isalpha())
        f=0
        b=len(s)-1
        while f<b:
            if s[f]!=s[b]:
                return False 
            f+=1
            b-=1
        return True
print(isPalindrome("Was it a car or a cat I saw"))