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

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self._previous

    @previous_item.setter
    def previous_item(self, value):
        self._previous = value
        value._next = self

    def __repr__(self):
        return repr(self.track)


class LinkedList:
    """Связный список"""

    head = None
    tail = None

    def __init__(self, first_item=None):
        self.head = first_item
        self.tail = first_item

    @property
    def last(self):
        """Последний элемент"""
        return self.tail

    def append_left(self, item):
        """Добавление слева"""
        if self.head is None:
            self.head = LinkedListItem(item)
            self.tail = LinkedListItem(item)
        else:
            new_item = LinkedListItem(item)
            self.head._previous = new_item
            new_item._next = self.head
            self.head = new_item

    def append_right(self, item):
        """Добавление справа"""
        if self.head is None:
            self.head = LinkedListItem(item)
            return item
        elif self.tail is None:
            self.tail = LinkedListItem(item)
            self.head.next_item = self.tail
            return item
        else:
            self.tail = LinkedListItem(item)
            new_item = self.tail.previous_item
            new_item.next_item = self.tail
            return item

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
            tmp_item = tmp_item.next
        return length

    def __iter__(self):
        new_item = self.head

        while new_item:  # Если есть элемент
            yield new_item.track  # "Выкидываемое" значение
            new_item = new_item._next  # Переход к следующему элементу

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


"""
    # УДАЛИТЬ
    def print_list(self):
        cur = self.first_item
        while cur:
            print(cur.track)
            cur = cur._next



dllist = LinkedList()
dllist.append_left(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append_left(5)

dllist.print_list()
print()
print(f"len = {dllist.length}")

dllist.__reversed__()
dllist.print_list()



node = LinkedListItem(5)
linked_list = LinkedList(node)
linked_list.append(7)
linked_list.append(8)
linked_list.print_list()
print(linked_list.length)


dllist = LinkedList()
dllist.append(4)
dllist.append(-3)
dllist.append(1)
dllist.append(25)
dllist.append(0)
dllist.append(10)

for number in dllist:
    print(number)

expected_len = 1
"""

dllist = LinkedList()
dllist.append(4)
dllist.append(-3)
dllist.append(1)
dllist.append(25)
dllist.append(0)
dllist.append(10)

for number in dllist:
    print(number)

