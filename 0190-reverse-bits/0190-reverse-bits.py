class Solution(object):
    def reverseBits(self, n):
        ans=0
        for i in range(32):
         last_bit = n & 1
         ans = ans << 1
         ans = ans | last_bit
         n = n >> 1
        return ans
        """
        :type n: int
        :rtype: int
        """
        