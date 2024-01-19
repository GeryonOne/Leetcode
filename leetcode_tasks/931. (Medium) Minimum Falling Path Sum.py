"""
Учитывая матрицу целых чисел размером n x n (n строк, n столбцов),
верните минимальную сумму любого падающего пути через матрицу.

Падающий путь начинается с любого элемента в первой строке и выбирает элемент в следующей строке, который находится
либо непосредственно снизу, либо по диагонали влево/вправо. Конкретно, следующий элемент после позиции
(строка, столбец) будет (строка + 1, столбец - 1), (строка + 1, столбец) или (строка + 1, столбец + 1).
"""


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])

        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                left = dp[i - 1][max(0, j - 1)]
                up = dp[i - 1][j]
                right = dp[i - 1][min(n - 1, j + 1)]
                dp[i][j] = matrix[i][j] + min(left, up, right)

        return min(dp[n - 1])


solution = Solution()
print(solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(solution.minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))

