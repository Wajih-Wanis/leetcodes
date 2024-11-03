class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k = len(s)
        while k>0:
            if s==goal:
                return True
            s=s[1:]+s[0]
            k-=1
        return False