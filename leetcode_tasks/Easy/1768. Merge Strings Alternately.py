"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        extra_symbols = ''
        cycle_index = 0

        if len(word1) > len(word2):
            cycle_index = len(word2)
            extra_symbols = word1[len(word2):]

        elif len(word2) > len(word1):
            cycle_index = len(word1)
            extra_symbols = word2[len(word1):]

        elif len(word1) == len(word2):
            cycle_index = len(word1)
            extra_symbols = ''

        result = ''

        for i in range(cycle_index):
            if word1[i] != '':
                result += word1[i]
            if word2[i] != '':
                result += word2[i]

        result += extra_symbols

        return result


solution = Solution()
# print(solution.mergeAlternately('abcd', 'ab'))
print(solution.mergeAlternately(word1 = "ab", word2 = "pqrs"))
