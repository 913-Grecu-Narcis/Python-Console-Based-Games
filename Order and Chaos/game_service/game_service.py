from repo.repository import Repo
import random


class GameService:
    def __init__(self, repo: Repo):
        self.__repo = repo

    def get_all(self):
        return self.__repo.get_all()

    def player_move(self, row, column, option):
        self.__repo.set_cell(row, column, option)

    def computer_move(self):
        if self.check_for_1_move_win() is None:
            cell = random.choice(self.get_all())

            while cell.value != '':
                cell = random.choice(self.get_all())

            value = random.choice(['X', 'O'])
            cell.value = value
            return cell

        else:
            cell, value = self.check_for_1_move_win()
            cell.value = 'X' if value == 'O' else 'O'

            return cell


    def get_row(self, row_index):
        row = []

        for cell in self.get_all():
            if cell.row == row_index:
                row.append(cell)

        return row

    def get_column(self, column_index):
        column = []

        for cell in self.get_all():
            if cell.column == column_index:
                column.append(cell)

        return column

    def get_first_diagonal(self, row, column):
        diagonal = []

        for cell in self.get_all():
            if cell.row - cell.column == row - column:
                diagonal.append(cell)

        return diagonal

    def get_second_diagonal(self, row, column):
        diagonal = []

        for cell in self.get_all():
            if cell.row + cell.column == row + column:
                diagonal.append(cell)

        return diagonal

    @staticmethod
    def check_for_consecutive(cells):
        if len(cells) < 5:
            return False

        index = 0
        for i in range(len(cells)):
            if cells[i].value != '':
                index = i
                break

        length = 1
        max_length = 0

        for i in range(index + 1, len(cells)):
            if cells[i].value == cells[i - 1].value and cells[i].value != '':
                length += 1

            else:
                max_length = max(length, max_length)
                length = 1

        max_length = max(max_length, length)

        if max_length >= 5:
            return True

        return False


    def check_for_1_move_win(self):
        for cell in self.get_all():
            if cell.value == '':
                for ch in ['X', 'O']:
                    cell.value = ch

                    row = self.get_row(cell.row)
                    column = self.get_column(cell.column)
                    diagonal1 = self.get_first_diagonal(cell.row, cell.column)
                    diagonal2 = self.get_second_diagonal(cell.row, cell.column)

                    if self.check_for_consecutive(row):
                        cell.value = ''
                        return cell, ch

                    if self.check_for_consecutive(column):
                        cell.value = ''
                        return cell, ch

                    if self.check_for_consecutive(diagonal1):
                        cell.value = ''
                        return cell, ch

                    if self.check_for_consecutive(diagonal2):
                        cell.value = ''
                        return cell, ch

                cell.value = ''

        return None

    def check_if_board_is_full(self):
        for cell in self.get_all():
            if cell.value == '':
                return False

        return True

    def check_for_win(self):
        for cell in self.get_all():
            row = self.get_row(cell.row)
            column = self.get_column(cell.column)
            diagonal1 = self.get_first_diagonal(cell.row, cell.column)
            diagonal2 = self.get_second_diagonal(cell.row, cell.column)

            if self.check_for_consecutive(row):
                return True

            if self.check_for_consecutive(column):
                return True

            if self.check_for_consecutive(diagonal1):
                return True

            if self.check_for_consecutive(diagonal2):
                return True

        return False

    def save_file(self):
        self.__repo.save_board()

    def load_file(self):
        self.__repo.load_board()
