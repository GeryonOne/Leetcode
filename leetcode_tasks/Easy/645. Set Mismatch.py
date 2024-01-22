"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, 
one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
"""""

from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        incorrect_nums = []
        double_num, missing_num = 0, 0

        correct_set = [num for num in range(1, len(nums) + 1)]
        nums_count = Counter(nums)

        for i in range(1, len(correct_set) + 1):

            if nums_count[i] > 1:
                double_num = i

            if i not in nums_count:
                missing_num = i

        incorrect_nums.append(double_num)
        incorrect_nums.append(missing_num)

        return incorrect_nums


solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))
print(solution.findErrorNums([2, 2]))
print(solution.findErrorNums([1, 1]))
