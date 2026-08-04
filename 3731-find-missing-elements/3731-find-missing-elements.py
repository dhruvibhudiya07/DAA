class Solution(object):
    def findMissingElements(self, nums):
        missing=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                missing.append(i)
        return missing
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        