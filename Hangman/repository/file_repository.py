from repository.repository import Repo


class FileRepo(Repo):
    def __init__(self, file_name):
        super().__init__()

        self.__file_name = file_name
        self.load_file()

    def load_file(self):
        try:
            file = open(self.__file_name, 'rt')
        except IOError:
            return

        for line in file.readlines():
            new_line = line.strip()

            if new_line == '':
                continue

            super().add(new_line)

        file.close()

    def save_file(self):
        file = open(self.__file_name, 'wt')

        for sentence in super().get_all():
            file.write(sentence + '\n')

        file.close()

    def add(self, sentence):
        super().add(sentence)

        self.save_file()

    def delete(self, sentence):
        super().delete(sentence)

        self.save_file()

    def get_all(self):
        return super().get_all()
