from business.service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    def add_option(self, question_args):
        if len(question_args) != 7:
            print('Invalid number of arguments!'
                  'Enter command as: add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>')
            return

        try:
            id = int(question_args[0])
        except ValueError:
            print('Id must be an integer')
            return

        text = question_args[1]
        answers = question_args[2:5]
        correct_answer = question_args[5]
        difficulty = question_args[6]

        try:
            self.__service.add_question(id, text, answers, correct_answer, difficulty)
        except ValueError as ve:
            print(str(ve))

    def create_option(self, command_args):
        if len(command_args) != 2:
            print('Invalid number of arguments!')
            return

        command_args.extend(command_args[1].split())
        command_args.pop(1)

        if len(command_args) != 4:
            print('Invalid number of arguments!')
            return

        difficulty = command_args[1]
        try:
            number_of_questions = int(command_args[2])
        except ValueError:
            print('Number of questions must be an integer!')
            return

        file_name = command_args[3]

        self.__service.create_quiz(difficulty, number_of_questions, file_name)


    @staticmethod
    def print_question(question):
        print(f'{question.text}\n'
              f'Answers: {question.answers[0]}, {question.answers[1]}, {question.answers[2]}.')


    def quiz_menu(self, quiz):
        quiz_answers = []
        for question in quiz:
            self.print_question(question)
            answer = input('Your answer is: ')

            quiz_answers.append(answer)

        score = self.__service.compute_score(quiz, quiz_answers)

        print(f'\nCongrats!\n'
              f'Your score is: {score}!')


    def main_menu(self):
        while True:
            command = input('>>>')

            command_args = command.strip().split(maxsplit=1)

            if command_args[0] == 'add':
                question_args = command_args[1].split(';')
                print(question_args)
                self.add_option(question_args)

            elif command_args[0] == 'create':
                self.create_option(command_args)

                print(command_args)
                pass

            elif command_args[0] == 'start':
                print(command_args)
                quiz = self.__service.start_quiz(command_args[1])

                if len(quiz) == 0:
                    print('Quiz does not exist or is empty!')

                else:
                    self.quiz_menu(quiz)
                pass

            elif command_args[0] == 'exit':
                break
