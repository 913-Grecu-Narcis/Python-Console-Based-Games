from domain.cell import Cell


class Repo:
    def __init__(self, file_name='board.txt'):
        self.__board = [Cell(i, j) for i in range(6) for j in range(6)]
        self.__file_name = file_name

    def get_all(self):
        return self.__board

    def get_cell(self, row, column):
        for cell in self.__board:
            if cell.row == row and cell.column == column:
                return cell

        return None

    def set_cell(self, row, column, value):
        cell = self.get_cell(row, column)

        if cell is None:
            raise ValueError('Place not in board!')

        if cell.value != '':
            raise ValueError('Cell already used!')

        if value not in ['X', 'O']:
            raise ValueError('Symbol is not X or O!')

        cell.value = value

    def save_board(self):
        file = open(self.__file_name, 'wt')

        counter = 0
        for cell in self.get_all():
            counter += 1
            if cell.value == '':
                file.write('-' + ' ')
            file.write(cell.value + ' ')

            if counter == 6:
                counter = 0
                file.write('\n')

    def load_board(self):
        try:
            file = open(self.__file_name, 'rt')
        except IOError:
            return

        for i in range(6):
            line = file.readline()

            values = line.strip().split()
            for j in range(6):
                cell = self.get_cell(i, j)

                if values[j] == '-':
                    cell.value = ''
                else:
                    cell.value = values[j]
