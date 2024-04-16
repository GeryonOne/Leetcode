class InnerDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value


# Использование объекта как словаря
obj = InnerDict()
obj['key1'] = 'value1'  # Установка значения
print(obj['key1'])      # Получение значения