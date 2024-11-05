class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        comp = ""
        if not word:
            return None
        cur = word[0]
        i= 1
        while i<len(word):
            if cur == word[i]:
                count+=1
            else:
                while count >9:
                    comp += str(9) + cur
                    count -= 9
                comp+= str(count) + cur
                cur = word[i]
                count = 1
            i+=1
        while count >9:
            comp += str(9) + cur
            count -= 9
        comp+= str(count) + cur
    
        return comp