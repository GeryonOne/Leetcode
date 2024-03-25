"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

This solution beats 99.65% of users in Python
"""


class Solution(object):

    def count_bits(self, decimal_number):
        bin_num = format(decimal_number, 'b')
        count_bits = bin_num.count('1')

        return count_bits

    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()

        sorted_list = list(sorted(arr, key=lambda x: self.count_bits(x)))

        return sorted_list


solution = Solution()
print(solution.sortByBits([0,1,2,3,4,5,6,7,8]))
print(solution.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))

