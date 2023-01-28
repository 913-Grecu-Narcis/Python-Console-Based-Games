class Question:
    def __init__(self, id, text, answers, correct_answer, difficulty):
        self.__id = id
        self.__text = text
        self.__answers = answers
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @property
    def answers(self):
        return self.__answers

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def difficulty(self):
        return self.__difficulty

    def __lt__(self, other):
        if self.__difficulty == 'easy':
            return True

        if self.__difficulty == 'medium' and other.__difficulty in ['medium', 'hard']:
            return True

        if self.__difficulty == 'hard' and other.__difficulty == 'hard':
            return True

        return False
