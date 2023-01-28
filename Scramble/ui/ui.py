from service.game_service import Service

class UI:
    def __init__(self, service: Service):
        self.__service = service

    def play_game(self):
        self.__service.select_sentence()
        self.__service.scramble_sentence()

        while True:
            print(self.__service.get_sentence())
            print(self.__service.get_scrambled_sentence(), f'(Score is: {self.__service.get_score()})')
            command = input('>>>')

            command_args = command.strip().split()

            for arg in command_args:
                arg.strip()

            if command_args[0] == 'undo':
                try:
                    self.__service.undo()
                except ValueError as ve:
                    print(str(ve))

            elif command_args[0] == 'swap':
                if len(command_args) != 6:
                    print('Invalid numbers of arguments!')
                    continue

                try:
                    word1 = int(command_args[1])
                    letter1 = int(command_args[2])

                    word2 = int(command_args[4])
                    letter2 = int(command_args[5])
                except ValueError:
                    print('Invalid arguments!')
                    continue

                try:
                    self.__service.make_swap(word1, letter1, word2, letter2)
                except ValueError as ve:
                    print(str(ve))

            else:
                print('Invalid command!')

            game_status = self.__service.check_if_game_over()
            if game_status == -1:
                print('You lost!')
                break

            elif game_status == 1:
                print(f'You won! (Score: {self.__service.get_score()})')
                break
