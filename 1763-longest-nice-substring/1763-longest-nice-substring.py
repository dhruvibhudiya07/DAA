class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s)<2:
            return ""
        letters=set(s)
        for i in range(len(s)):
            if s[i].lower() not in letters or s[i].upper() not in letters:#if both case is missing
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        # If every letter has both uppercase and lowercase
        return s

        """
        :type s: str
        :rtype: str
        """
        