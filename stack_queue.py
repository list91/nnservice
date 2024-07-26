class StackQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Добавление элемента в конец списка
        self.items.append(item)

    def dequeue(self):
        # Извлечение элемента с конца списка (последнего добавленного элемента)
        if len(self.items) == 0:
            raise IndexError("Извлечение из пустой очереди невозможно")
        return self.items.pop()

    def __len__(self):
        # Возвращает количество элементов в очереди
        return len(self.items)