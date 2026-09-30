class Solution(object):
    def longestPalindrome(self, s):
        longest = "" 
        for i in range(len(s)): 
            for j in range(i, len(s)): 
                sub = s[i:j+1] 
                if sub == sub[::-1]: 
                    if len(sub) > len(longest): 
                       longest = sub 
        return longest

        """
        :type s: str
        :rtype: str
        """
        