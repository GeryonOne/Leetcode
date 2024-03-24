"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""""


"""
Needs optimization, fix later
"""
class Solution(object):

    def is_palindrome(self, string):
        """
        :param string:
        :return: str
        """

        if string == string[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s

        palindrome_subs = []

        for i in range(len(s)):
            curr_substring = s[i]
            for j in range(i + 1, len(s)):
                check_substring = s[i:j+1]
                if self.is_palindrome(check_substring):
                    curr_substring = check_substring
            palindrome_subs.append(curr_substring)

        return max(palindrome_subs, key=len)


solution = Solution()
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('cbbd'))
print(solution.longestPalindrome('s'))