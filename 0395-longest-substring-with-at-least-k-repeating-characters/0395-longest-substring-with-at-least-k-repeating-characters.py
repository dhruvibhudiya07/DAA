class Solution(object):
    def longestSubstring(self, s, k):
        ans = 0
        for unique in range(1, 27):
            count = [0] * 26
            left = 0
            right = 0
            unique_count = 0
            valid_count = 0
            while right < len(s):
                index = ord(s[right]) - ord('a')
                if count[index] == 0:
                    unique_count += 1
                count[index] += 1
                if count[index] == k:
                    valid_count += 1
                right += 1
                while unique_count > unique:
                    index = ord(s[left]) - ord('a')
                    if count[index] == k:
                        valid_count -= 1
                    count[index] -= 1
                    if count[index] == 0:
                        unique_count -= 1
                    left += 1
                if unique_count == unique and valid_count == unique:
                    ans = max(ans, right - left)
        return ans
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        