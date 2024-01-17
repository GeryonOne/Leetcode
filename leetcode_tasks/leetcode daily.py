"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        step_count = 0

        for symbol in s:
            s_dict[symbol] = s_dict.get(symbol, 0) + 1

        for symbol in t:
            t_dict[symbol] = t_dict.get(symbol, 0) + 1

        for key in s_dict:
            step_count += max(0, s_dict.get(key, 0) - t_dict.get(key, 0))

        return step_count


solution = Solution()
print(solution.minSteps("bba", "aba"))
print(solution.minSteps("leetcode_tasks", "practice"))
print(solution.minSteps("anagram", "mangaar"))
