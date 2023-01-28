import random

from domain.question import Question
from infrastructure.file_repo import FileRepo
import copy

class Service:
    def __init__(self, repo: FileRepo):
        self.__repo = repo


    def add_question(self, id, text, answers, correct_answer, difficulty):
        question = Question(id, text, answers, correct_answer, difficulty)

        self.__repo.add(question)


    def __count_by_difficulty(self, difficulty):
        counter = 0

        for question in self.__repo.get_all():
            if question.difficulty == difficulty:
                counter += 1

        return counter


    def __get_questions(self, difficulty, number_of_questions):
        questions = copy.deepcopy(self.__repo.get_all())
        quiz = []

        half = number_of_questions // 2 + number_of_questions % 2

        while len(quiz) < half:
            question = random.choice(questions)
            questions.remove(question)

            if question.difficulty == difficulty:
                quiz.append(question)

        while len(quiz) < number_of_questions:
            question = random.choice(questions)
            questions.remove(question)
            quiz.append(question)

        return quiz


    @staticmethod
    def __save_quiz_to_file(quiz, file_name):
        with open(file_name, 'wt') as file:
            for question in quiz:
                file.write(f'{question.id};{question.text};{question.answers[0]};{question.answers[1]};'
                           f'{question.answers[2]};{question.correct_answer};{question.difficulty}\n')


    def create_quiz(self, difficulty, number_of_questions, file_name):
        if difficulty not in ['easy', 'medium', 'hard']:
            raise ValueError('Difficulty is not easy/medium/hard!')

        if number_of_questions <= 0:
            raise ValueError('Number of questions must be an positive integer!')

        if len(self.__repo) < number_of_questions:
            raise ValueError(f'Quiz cannot be created because there are not at least {number_of_questions} questions!')


        question_with_difficulty = self.__count_by_difficulty(difficulty)

        if question_with_difficulty < number_of_questions // 2 + number_of_questions % 2:
            raise ValueError(f'Quiz cannot be created because there are not at least '
                             f'{number_of_questions // 2 + number_of_questions % 2} '
                             f'questions with difficulty {difficulty}!')

        quiz = self.__get_questions(difficulty, number_of_questions)

        self.__save_quiz_to_file(quiz, file_name)


    @staticmethod
    def __load_quiz(file_name):
        quiz = []

        try:
            file = open(file_name, 'rt')
        except IOError:
            return quiz

        for line in file.readlines():
            question_args = line.strip().split(';')

            id = int(question_args[0])
            text = question_args[1]
            answers = question_args[2:5]
            correct_answer = question_args[5]
            difficulty = question_args[6]

            question = Question(id, text, answers, correct_answer, difficulty)
            quiz.append(question)

        return quiz


    def start_quiz(self, file_name):
        quiz = self.__load_quiz(file_name)

        sorted_quiz = sorted(quiz)

        return sorted_quiz

    @staticmethod
    def compute_score(quiz, quiz_answers):
        score = 0
        for i in range(len(quiz)):
            if quiz[i].correct_answer == quiz_answers[i]:
                if quiz[i].difficulty == 'easy':
                    score += 1

                elif quiz[i].difficulty == 'medium':
                    score += 2

                elif quiz[i].difficulty == 'hard':
                    score += 3

        return score
