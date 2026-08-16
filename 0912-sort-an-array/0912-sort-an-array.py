class Solution(object):
    def sortArray(self, nums):
        def merging(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result
        def divide(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            return merging(left, right)
        return divide(nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        