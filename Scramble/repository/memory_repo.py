class MemoryRepo:
    def __init__(self):
        self._data = []

    def find(self, sentence):
        for item in self._data:
            if sentence == item:
                return item

        return None

    def add(self, sentence):
        if self.find(sentence) is not None:
            raise ValueError('Sentence already in repo!')

        self._data.append(sentence)

    def get_all(self):
        return self._data
