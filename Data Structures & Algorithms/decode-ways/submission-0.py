class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[n] = 1                                  # empty suffix -> 1 way
        dp[n - 1] = 1 if s[n - 1] != "0" else 0     # last char alone

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp[i] = 0                            # '0' can't start a valid code
            elif s[i] == "1":
                dp[i] = dp[i + 1] + dp[i + 2]         # 10-19 always valid
            elif s[i] == "2":
                if s[i + 1] <= "6":
                    dp[i] = dp[i + 1] + dp[i + 2]     # 20-26 valid as pair
                else:
                    dp[i] = dp[i + 1]                 # 27-29 only single digit
            else:
                dp[i] = dp[i + 1]                     # 3-9 only single digit

        return dp[0]