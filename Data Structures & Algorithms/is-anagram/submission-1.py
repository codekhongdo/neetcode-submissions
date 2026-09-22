class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        if (len(a)!=len(b)):
            return False
        for i in range (len(a)):
            if (a[i]==b[i]):
                continue
            else:
                return False
        return True
