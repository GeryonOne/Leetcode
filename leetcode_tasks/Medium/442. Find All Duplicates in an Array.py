'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears 
once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]
'''""


from collections import Counter  # Необходимо для второго решения

class Solution(object):
    def findDuplicates(self, nums):

        count_dict = {}
        result_list = []

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > 1:
                result_list.append(num)

        return result_list


# 2-е решение, с использованием класса Counter:
# class Solution(object):
#     def findDuplicates(self, nums):
#         count_dict = Counter(nums)
#         result_list = [num for num, count in count_dict.items() if count > 1]
#         return result_list
