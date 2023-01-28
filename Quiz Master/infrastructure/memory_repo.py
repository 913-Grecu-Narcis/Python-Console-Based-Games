class MemoryRepo:
    def __init__(self):
        self.__data = []

    def find_by_id(self, item_id):
        for item in self.__data:
            if item.id == item_id:
                return item

        return None

    def add(self, item):
        if self.find_by_id(item.id) is not None:
            raise ValueError(f'Item with id {item.id} already in repo!')

        self.__data.append(item)

    def remove_by_id(self, item_id):
        item = self.find_by_id(item_id)

        if item is None:
            raise ValueError(f'Item with id {item_id} not in repo!')

        self.__data.remove(item)

    def get_all(self):
        return self.__data

    def __len__(self):
        return len(self.__data)
