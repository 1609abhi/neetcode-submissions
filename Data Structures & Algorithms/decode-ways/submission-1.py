class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1 if s[0] != "0" else 0

        dp = [0 for _ in range(n)]
        dp[n-1] = 1 if s[-1] != "0" else 0
        dp[n-2] = (dp[n-1] if s[-2] != "0" else 0) + (1 if 10 <= int(s[-2:]) <= 26 else 0)

        for i in range(n-3, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == "2":
                if int(s[i+1]) <= 6:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1]
        return dp[0]