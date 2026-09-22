class Solution:
    def isPalindrome(self, s: str) -> bool:
        A=[]
        B=[]
        for i in s:
            if i.isalnum():
               A.append(i.lower())
        a="".join(A)
        for k in s[::-1]:
            if k.isalnum():
               B.append(k.lower())
        b="".join(B)
        if a==b:
            return True
        else:
            return False
