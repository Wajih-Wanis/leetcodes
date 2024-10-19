class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        stack = []
        s = "0"
        while n>0:
            for c in s:
                if c == "0":
                    stack.append("1")
                else:
                    stack.append("0")
            
            s+= "1"
            while stack:
                s+=stack.pop()
            n-=1
        return s[k-1]