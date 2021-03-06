"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """

        s = 'pwwek'
        buff = {
            'p': 0,
            'w': 1,
        }

        :type s: str
        :rtype: int
        """
        length = len(s)

        if length <= 1:
            return length

        head = 0
        tail = 1
        max_length = 1
        buff = {s[head]: head}

        while tail < length:
            ch = s[tail]
            if ch in buff and head <= buff[ch] < tail:
                head = buff[ch] + 1
            if (tail-head+1) > max_length:
                max_length = tail - head + 1

            buff[ch] = tail
            tail += 1

        return max_length


solution = Solution()
testcases = [
    ('bbbbb', 1),
    ('abcabcbb', 3),
    ('pwwkew', 3),
    ('au', 2),
]

for case, expect in testcases:
    val = solution.lengthOfLongestSubstring(case)
    print '%10s => %d (%s)' % (case, val, val==expect)
    # assert val == expect, '%s expect %d, but given %d' % (case, expect, val)
