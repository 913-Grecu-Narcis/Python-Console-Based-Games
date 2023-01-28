from game_service.game_service import GameService
import prettytable


class UI:
    def __init__(self, service: GameService):
        self.__service = service

    def print_board(self):
        table = prettytable.PrettyTable(['C1', 'C2', 'C3', 'C4', 'C5', 'C6'])
        table.hrules = prettytable.ALL
        table.header = False
        width = 3
        table._min_width = {'C1': width, 'C2': width, 'C3': width, 'C4': width, 'C5': width, 'C6': width}
        board = self.__service.get_all()

        for i in range(6):
            table.add_row(board[i*6:(i+1)*6])

        print(table)


    def check_if_game_over(self):
        if self.__service.check_for_win():
            print('Order won!')
            return True

        if self.__service.check_if_board_is_full():
            print('Chaos won!')
            return True

        return False

    @staticmethod
    def print_help():
        print("Type 'save' to save the board to file.\n"
              "Enter a triple 'row column symbol' to place a symbol at position (row, column).")

    def main_menu(self):
        while True:
            print('Press 1 to start a new game.\n'
                  'Press 2 to load a game.\n')

            option = input('Your option is: ')

            if option in ['1', '2']:
                break

        if option == '2':
            self.__service.load_file()

        self.play_game()


    def play_game(self):
        while True:
            self.print_board()

            print('Player turn...')
            command = input('>>>')

            cmd_args = command.strip().split()

            if len(cmd_args) == 1:
                if cmd_args[0] == 'help':
                    UI.print_help()

                elif cmd_args[0] == 'save':
                    self.__service.save_file()
                    # save to file
                else:
                    print('Type help for available commands!')

            elif len(cmd_args) == 3:
                try:
                    row = int(cmd_args[0])
                    column = int(cmd_args[1])
                    option = cmd_args[2]

                except ValueError:
                    print('Row and column must be integers between 1 and 6!\n'
                          'Type help for available commands!')
                    continue

                try:
                    self.__service.player_move(row - 1, column - 1, option)
                except ValueError as ve:
                    print(str(ve))
                    continue

                if self.check_if_game_over():
                    self.print_board()
                    break

                cell = self.__service.computer_move()
                print(f'AI: ({cell.row}, {cell.column}, {cell.value})')
                if self.check_if_game_over():
                    self.print_board()
                    break

            else:
                print('Invalid command!\n'
                      'Type help for available commands!')
