class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        answer = []
        for i in range(k):
            max_num = max(count, key=count.get)
            answer.append(max_num)
            del count[max_num]
        return answer
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        