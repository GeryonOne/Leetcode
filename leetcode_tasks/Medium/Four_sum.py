from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    result_set = set()
    nums.sort()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left, right = j + 1, len(nums) - 1

            while left < right:
                current_expression = nums[i] + nums[j] + nums[left] + nums[right]
                current_quadro = (nums[i], nums[j], nums[left], nums[right])
                if current_expression == target:
                    result_set.add(current_quadro)
                    left += 1
                    right -= 1
                    continue
                elif current_expression < target:
                    left += 1
                elif current_expression > target:
                    right -= 1

    return list(result_set)


print(fourSum([1,0,-1,0,-2,2], 0))

