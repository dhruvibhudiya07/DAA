class Solution(object):
    def maxSubArray(self, nums):
        currentsum=nums[0]
        maxsum=nums[0]
        for i in range (1,len(nums)):
            currentsum=max(nums[i],currentsum+nums[i])
            maxsum=max(maxsum,currentsum)
        return maxsum
        """
        :type nums: List[int]
        :rtype: int
        """
        