class UndoService:
    def __init__(self):
        self.__operations = []

    def add_operation(self, word1, letter1, word2, letter2):
        self.__operations.append([word1, letter1, word2, letter2])

    def get_last_operation(self):
        if len(self.__operations) == 0:
            raise ValueError('No operation to undo!')

        return self.__operations.pop()
