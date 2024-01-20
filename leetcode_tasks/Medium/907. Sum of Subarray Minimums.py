"""
Важно: задача не решена полностью, не проходит тяжеловесные тесты

Дан массив целых чисел arr. Найдите сумму min(b), где b охватывает каждый (смежный) подмассив arr. Поскольку ответ
может быть большим, верните ответ по модулю 10**9 + 7.

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
"""""


from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        subarrays = []
        mins_sum = 0
        mod = 10 ** 9 + 7
        n = len(arr)

        for i in range(n):
            for j in range(i, n + 1):
                if arr[i:j]:
                    subarrays.append(arr[i:j])

        for array in subarrays:
            mins_sum += min(array)

        result = mins_sum % mod
        return result


solution = Solution()
print(solution.sumSubarrayMins([71, 55, 82, 55]))