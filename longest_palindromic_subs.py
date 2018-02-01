"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"

    Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        buff = {}
        i = 0
        longest = []
        for ch in s:
            if ch in buff:
                if len(buff[ch]) == 2 and i > buff[ch][1]:
                    buff[ch][1] = i
                else:
                    buff[ch].append(i)
            else:
                buff[ch] = [i]
            i += 1
        return buff


# s = 'cbbd'
s = 'bcbd'
solution = Solution()
print solution.longestPalindrome(s)
