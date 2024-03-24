"""
Учитывая целочисленную матрицу grid размером n x n, вернуть минимальную сумму падающего пути с ненулевыми сдвигами.

Падающий путь с ненулевыми сдвигами представляет собой выбор ровно одного элемента из каждой строки матрицы grid так,
что никакие два выбранных элемента в соседних строках не находятся в одном и том же столбце.
"""

from typing import List


class Solution:

    def find_min(self, curr_row, del_index):
        min_num = float('inf')

        for index, num in enumerate(curr_row):
            if index == del_index:
                continue

            if num < min_num:
                min_num = num

        return min_num

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])

        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                prew_min_num = self.find_min(dp[i - 1], j)
                dp[i][j] = matrix[i][j] + prew_min_num  # передать сюда индекс, сравнивать их при сложении

        return min(dp[n - 1])


solution = Solution()
print(solution.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
