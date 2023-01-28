from repository.memory_repo import MemoryRepo


class FileRepo(MemoryRepo):
    def __init__(self, file_name='input.txt'):
        super().__init__()
        self.__file_name = file_name

        self.load_file()

    def load_file(self):
        try:
            file = open(self.__file_name, 'rt')
        except IOError:
            return

        for line in file.readlines():
            sentence = line.strip()

            if sentence == '':
                continue

            super().add(sentence)

        file.close()

