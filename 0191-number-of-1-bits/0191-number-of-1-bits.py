class Solution(object):
    def hammingWeight(self, n):
        count = 0 
        for i in range(32):
            if n & 1:
                count +=1
            n >>= 1
        return count 
        """
        :type n: int
        :rtype: int
        """
        