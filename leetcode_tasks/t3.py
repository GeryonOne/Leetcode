"""
Реализуйте класс RandomizedSet:

1. RandomizedSet() Инициализирует объект RandomizedSet.
2. bool insert(int val) Вставляет элемент val в множество, если его там нет. Возвращает true, если элемент не был в множестве, в противном случае возвращает false.
3. bool remove(int val) Удаляет элемент val из множества, если он там присутствует. Возвращает true, если элемент был в множестве, в противном случае возвращает false.
4. int getRandom() Возвращает случайный элемент из текущего набора элементов (гарантируется, что хотя бы один элемент существует, когда вызывается этот метод). Каждый элемент должен иметь одинаковую вероятность быть выбранным.
Необходимо реализовать функции класса таким образом, чтобы каждая функция работала в среднем за O(1) времени.
"""""
import random

class RandomizedSet:

    def __init__(self):
        self.my_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.my_set:
            self.my_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.my_set:
            self.my_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.sample(self.my_set, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()