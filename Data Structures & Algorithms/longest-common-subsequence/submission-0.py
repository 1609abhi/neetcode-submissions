class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp=[[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        maxi=0
        for index1 in range(1,len(text1)+1):
            for index2 in range(1,len(text2)+1):
                if text1[index1-1]==text2[index2-1]:
                    dp[index1][index2]=1+dp[index1-1][index2-1]
                    maxi=max(maxi,dp[index1][index2])
                else:
                    dp[index1][index2]=max(dp[index1-1][index2],dp[index1][index2-1])

        return maxi

