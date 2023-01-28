class Repo:
    def __init__(self):
        self.__sentences = []

    def find(self, sentence):
        for s in self.__sentences:
            if s == sentence:
                return s

        return None

    def add(self, sentence):
        if self.find(sentence) is not None:
            raise ValueError('Duplicate sentence!')

        self.__sentences.append(sentence)

    def delete(self, sentence):
        if self.find(sentence) is None:
            raise ValueError('Sentence not found!')

        self.__sentences.remove(sentence)

    def get_all(self):
        return self.__sentences
