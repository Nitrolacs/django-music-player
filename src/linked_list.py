"""
Модуль, реализующий двусвязный списком
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

        if value:
            if self._next != value:
                self._next = value
                value.previous_item = self
        else:
            self._next = None

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self._previous

    @previous_item.setter
    def previous_item(self, value):
        if value:
            if self._previous != value:
                self._previous = value
                value.next_item = self
        else:
            self._previous = None

    def track(self):
        return self.track



class LinkedList:
    """Двусвязный список"""

    def __init__(self, first_item=None):
        self.first_item = None
        self.items_count = 0
        if first_item:
            self.append(first_item)

    @property
    def last(self):
        """Последний элемент"""
        last_element = None
        if self.first_item:
            last_element = self.first_item.previous_item
        return last_element

    def append_left(self, item):
        """Добавление элемента в начало списка"""
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(item)

        if not self.first_item:
            self.first_item = item
            self.first_item.next_item = self.first_item
            self.first_item.previous_item = self.first_item

        else:
            self.first_item.previous_item.next_item = item
            item.next_item = self.first_item
            self.first_item = self.first_item.previous_item

    def append_right(self, item):
        """Добавление элемента в конец списка"""
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(item)

        if not self.first_item:
            self.first_item = item

            if self.first_item.next_item:
                current = self.first_item

                while current.next_item != self.first_item:
                    current = current.next_item

                self.first_item.previous_item = current
                current.next_item = self.first_item
            else:
                self.first_item.previous_item = self.first_item
        else:
            self.first_item.previous_item.next_item = item
            item.next_item = self.first_item

    def append(self, item):
        """Добавление справа"""
        self.append_right(item)

    def remove(self, item):
        """Удаление элемента"""
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(item)

        if self.first_item:

            if item.track == self.first_item.track:

                if self.first_item.next_item == self.first_item:
                    self.first_item = None
                else:
                    remove_item = self.first_item
                    self.first_item = self.first_item.next_item
                    remove_item.next_item.previous_item = remove_item.previous_item
                    remove_item.next_item = None
                    remove_item.previous_item = None
            else:
                cur_item = self.first_item.next_item
                exception = True
                while cur_item != self.first_item:
                    if cur_item.track == item.track:
                        exception = False
                        break
                    cur_item = cur_item.next_item

                if not exception:
                    remove_item = cur_item
                    remove_item.next_item.previous_item = remove_item.previous_item
                    remove_item.next_item = None
                    remove_item.previous_item = None
                else:
                    raise ValueError()
        else:
            raise ValueError()

    def insert(self, previous, item):
        """Вставка справа"""
        raise NotImplementedError()

    def __len__(self):
        """Длина списка"""
        length = 0
        if self.first_item:
            length += 1
            cur = self.first_item
            while cur.next_item != self.first_item:
                length += 1
                cur = cur.next_item
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
        head = self.first_item
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
