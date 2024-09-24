class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_1 = set()
        
        for d in arr1:
            while d not in prefix_1 and d>0:
                prefix_1.add(d)
                d //= 10
        
        longest = 0
        for d in arr2:
            while d>0:
                if d in prefix_1 and len(str(d))>longest:
                    longest = len(str(d))
                d//=10
                    
        
        
        return longest