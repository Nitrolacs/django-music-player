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

    def __repr__(self):
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
            self.last.next_item = item
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
        if self.first_item:
            if not isinstance(item, LinkedListItem):
                item = LinkedListItem(item)
            if self.first_item == previous:
                self.first_item.next_item.previous_item = item
                self.first_item.next_item = item
            else:
                cur_item = self.first_item
                while cur_item.previous_item != previous:
                    cur_item = cur_item.previous_item
                cur_item.previous_item.next_item = item
                cur_item.previous_item = item
        else:
            raise ValueError()

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
        """Поддержка итерации"""
        new_item = self.first_item

        while new_item:  # Если есть элемент
            if new_item.next_item != self.first_item:
                yield new_item.track  # "Выкидываемое" значение
                new_item = new_item.next_item  # Переход к следующему элементу
            else:
                yield new_item.track
                break

    def __next__(self):
        """Возврат следующего элемента"""
        if self.items_count == len(self):
            raise StopIteration()

        return_item = self[self.items_count]
        self.items_count += 1

    def __getitem__(self, index):
        """Возврат элемента по индексу"""
        if not self.first_item:
            raise IndexError()

        if index >= len(self):
            raise IndexError()

        if index < 0:
            index = index + len(self)
            if index < 0:
                raise IndexError()

        if not 0 <= index < len(self):
            raise IndexError()

        number = 0
        current = self.first_item

        while number != index:
            number += 1
            current = current.next_item

        return current

    def __contains__(self, item):
        """Добавляет поддержку оператора in"""

        new_item = self.first_item
        while new_item:
            if new_item.next_item != self.first_item:
                if new_item.track == item:
                    return True
                else:
                    new_item = new_item.next_item  # Переход к следующему элементу
            else:
                if new_item.track == item:
                    return True
                return False

    def __reversed__(self):
        head = self.first_item
        previous = None
        while head:
            tmp_head = head
            head = head.next_item
            tmp_head._next = previous
            tmp_head._previous = head
            previous = tmp_head
        self.first_item = previous

"""
dl_list = LinkedList()
dl_list.append(2)
dl_list.append(1)
dl_list.append(3)
dl_list.append(5)

# dl_list.__reversed__()
# print(dl_list.__contains__(10))
item = dl_list.__getitem__(1)
print(item)
print(f"type(item) == {type(item.track)}")

node_list = [2, 1, 3, 5]
item_new = node_list[1]
print(f"type(item_new) == {type(item_new)}")
print(item == item_new)
"""