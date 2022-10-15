"""
Модуль, реализующий операции над связным списком
"""


class LinkedListItem:
    """Узел связного списка"""

    def __init__(self, data=None):
        self.track = data
        self._previous = None
        self._next = None

    @property
    def next_item(self):
        """Следующий элемент"""
        return self._next

    @next_item.setter
    def next_item(self, value):
        self._next = value
        value._previous = self
        if value._next == self:
            value._next = None

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self._previous

    @previous_item.setter
    def previous_item(self, value):
        self._previous = value
        value._next = self
        if value._previous == self:
            value._previous = None

    def __repr__(self):
        return repr(self.track)


class LinkedList:
    """Связный список"""

    def __init__(self, first_item=None):
        while first_item:
            first_item = first_item.previous_item

        self.first_item = first_item

    @property
    def last(self):
        """Последний элемент"""
        raise NotImplementedError()

    def append_left(self, item):
        """Добавление слева"""

        if self.first_item is None:
            new_item = LinkedListItem(item)
            self.first_item = new_item
        else:
            new_item = LinkedListItem(item)
            self.first_item._previous = new_item
            new_item._next = self.first_item
            self.first_item = new_item

    def append_right(self, item):
        """Добавление справа"""

        if self.first_item is None:
            new_item = LinkedListItem(item)
            self.first_item = new_item
        else:
            new_item = LinkedListItem(item)
            current_item = self.first_item
            while current_item._next:
                current_item = current_item._next
            current_item._next = new_item
            new_item._previous = current_item

    def append(self, item):
        """Добавление справа"""
        return self.append_right(item)

    def remove(self, item):
        """Удаление"""
        raise NotImplementedError()

    def insert(self, previous, item):
        """Вставка справа"""
        raise NotImplementedError()

    def __len__(self):
        tmp_item = self.first_item
        length = 0
        while tmp_item:
            length += 1
            tmp_item = tmp_item.next_item
        return length

    def __iter__(self):
        new_item = self.first_item

        while new_item:  # Если есть элемент
            yield new_item.track  # "Выкидываемое" значение
            new_item = new_item.next_item  # Переход к следующему элементу

    def __next__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        head = self.head
        previous = None
        while head:
            tmp_head = head
            head = head._next
            tmp_head._next = previous
            tmp_head._previous = head
            previous = tmp_head
        self.first_item = previous

    def __repr__(self):
        return [number for number in self]

"""
node = LinkedListItem(0)
previous = node
first = node
node = LinkedListItem(1)
previous.next_item = node  # в этом моменте и у previous, и у first
                           # устанавливается значение _next равное 1, так как previous is first
                           # у node устанавливается значение _previous равное 0

previous = node  # у previous тоже будет значение _previous равняться 0, как и у node
previous.next_item = first
linked_list = LinkedList(first)
print(len(linked_list))  # должно получиться 2
"""