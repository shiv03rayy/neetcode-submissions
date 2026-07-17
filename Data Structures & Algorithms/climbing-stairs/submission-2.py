class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        # Step 1: create dp array of size ___
        dp = [0] * (n+1)
        
        # Step 2: base cases
        dp[1] = 1
        dp[2] = 2
        
        # Step 3: loop and fill
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        # Step 4: return answer
        return dp[n]