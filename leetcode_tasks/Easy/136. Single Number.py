"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num) == 1:
                return num

    # Оптимизированный метод: return 2 * sum(set(nums)) - sum(nums)


solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))
