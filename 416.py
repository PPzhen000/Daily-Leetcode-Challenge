class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        s = (totalSum//2) + 1
        n = len(nums) + 1
        dp = [[False for i in range(s)] for j in range(n)]
        for i in range(n):
            for j in range(s):
                if i == 0: 
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
        for i in range(1,n):
            for j in range(1,s):  
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]