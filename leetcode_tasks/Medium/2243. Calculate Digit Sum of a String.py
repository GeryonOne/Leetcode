"""
You are given a string s consisting of digits and an integer k.

A round can be completed if the length of s is greater than k. In one round, do the following:

1. Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on.
Note that the size of the last group can be smaller than k.

2. Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.

3. Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.

Return s after all rounds have been completed.
"""""


def return_sum(chunk):
    chunk_list = [int(i) for i in chunk]
    return str(sum(chunk_list))


def digitSum(s, k):
    # Выполнить 1-е условие: пока длина s больше k
    while len(s) > k:
        chunk_list = []

        # Разбить строку на отрезки длинною в k
        for chunk in range(0, len(s), k):
            chunk_list.append(s[chunk:chunk + k])

        # Заменить каждый отрезок на значение его суммы
        for i in range(len(chunk_list)):
            chunk_list[i] = return_sum(chunk_list[i])

        s = ''.join(chunk_list)

    return s

print(digitSum(s="11111222223", k=3))