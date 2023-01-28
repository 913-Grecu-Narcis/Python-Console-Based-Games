from service.game_service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    @staticmethod
    def print_menu():
        print('Press 1 to add a sentence.\n'
              'Press 2 to start the game.\n'
              'Press 3 to exit!')


    def main_menu(self):
        while True:
            UI.print_menu()
            # print(self.__service.start_game())

            choice = input('Your choice is: ')

            if choice == '1':
                self.menu_add()

            elif choice == '2':
                self.menu_game()

            elif choice == '3':
                break

            else:
                print('Invalid choice!')


    def menu_add(self):
        sentence = input('Enter the sentence you want to add: ')
        try:
            self.__service.add_sentence(sentence)
        except ValueError as ve:
            print(str(ve))

        print('Sentence added successfully!')


    @staticmethod
    def get_guess():
        guess = input('Your guess is: ')

        if len(guess) != 1:
            print('Please enter a letter!')
            UI.get_guess()

        elif guess < 'a' or guess > 'z':
            print('Please enter a lowercase letter!')
            UI.get_guess()

        return guess


    def menu_game(self):
        self.__service.start_game()

        while True:
            sentence = self.__service.make_hangman_sentence(self.__service.get_sentence())
            print(sentence, '-', self.__service.get_hangman())

            guess = self.get_guess()

            self.__service.make_guess(guess)

            result = self.__service.check_for_end()

            if result == -1:
                print('You lost! 😒')
                break

            elif result == 1:
                print('You won! 🎊🎊🎊')
                break
