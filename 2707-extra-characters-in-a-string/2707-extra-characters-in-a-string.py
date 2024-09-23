class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp = [ 0 for _ in range(len(s)+1)]
        
        hashy = set(dictionary)

        n = len(s)

        for i in range(n-1,-1,-1):
            
            dp[i] = dp[i+1] +1
            
            for l in range(1,n+1-i):
                if s[i:i+l] in hashy:
                    dp[i] = min(dp[i],dp[i+l])

            
        return dp[0]