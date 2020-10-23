class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        return self.find_helper(nums, S, memo)
    def find_helper(self, nums, S, memo):
        if (len(nums), S) in memo:
            return memo[(len(nums), S)]
        if not nums:
            if S == 0: return 1
            else: return 0
        answer = self.find_helper(nums[1:], S+nums[0], memo) + self.find_helper(nums[1:], S-nums[0], memo)
        memo[(len(nums), S)] = answer
        return answer

