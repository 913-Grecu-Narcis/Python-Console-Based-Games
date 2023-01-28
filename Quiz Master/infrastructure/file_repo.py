from domain.question import Question
from infrastructure.memory_repo import MemoryRepo


class FileRepo(MemoryRepo):
    def __init__(self, file_name='master question list.txt'):
        super().__init__()
        self.__file_name = file_name

        self.load_file()

    def load_file(self):
        try:
            file = open(self.__file_name, 'rt')
        except IOError:
            return

        for line in file.readlines():
            question = line.strip()
            if question == '':
                continue

            question_args = question.split(';')
            id = int(question_args[0])
            text = question_args[1]
            choices = question_args[2:5]
            correct_choice = question_args[5]
            difficulty = question_args[6]

            item = Question(id, text, choices, correct_choice, difficulty)

            super().add(item)

        file.close()

    def save_file(self):
        file = open(self.__file_name, 'wt')
        for question in self.get_all():
            file.write(f'{question.id};{question.text};{question.answers[0]};{question.answers[1]};'
                       f'{question.answers[2]};{question.correct_answer};{question.difficulty}\n')

        file.close()

    def add(self, item):
        super().add(item)
        self.save_file()

    def remove_by_id(self, item_id):
        super().remove_by_id(item_id)
        self.save_file()
