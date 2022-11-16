# Sudoku SOlver algorithm


class SudokuSolver():

    def __init__(self, board_string):

        self.BOARD_STRING = board_string
        self.BOARD_LENGTH = int(len(self.BOARD_STRING) ** .5)
        self.BOX_LENGTH = int(self.BOARD_LENGTH ** .5)

        self.board = []

        # Converts a board string into a board
        for row_i in range(self.BOARD_LENGTH):
            lbound, ubound = row_i * self.BOARD_LENGTH, (row_i + 1) * self.BOARD_LENGTH
            row = [int(char) for char in self.BOARD_STRING[lbound : ubound]]
            self.board.append(row)

    def get_board_string(self):

        output = ""
        for row in self.board:
            output += "".join(str(char) for char in row)
        return output

    def find_empty(self):

        # Returns the first empty cell in the board
        output = None
        for i in range(len(self.BOARD_STRING)):
            cell_i = (i // self.BOARD_LENGTH, i % self.BOARD_LENGTH)
            if not self.board[cell_i[0]][cell_i[1]]:
                output = cell_i
                break
        return output

    def solve(self):

        # Recursively fills in each empty cell with a valid permuation (p)
        output = False
        cell_i = self.find_empty()
        if cell_i:
            for p in range(1, self.BOARD_LENGTH + 1):
                if self.is_valid_cell(p, cell_i):
                    self.board[cell_i[0]][cell_i[1]] = p

                    if self.solve():
                        output = True
                        break
                    
                    self.board[cell_i[0]][cell_i[1]] = 0
        else:
            output = True
        return output
                
    def is_valid_cell(self, p, cell_i):

        output = True

        # Checks row
        for col_i in range(self.BOARD_LENGTH):
            if self.board[cell_i[0]][col_i] == p and col_i != cell_i[1]:
                output = False
                break

        # Checks column
        for row_i in range(self.BOARD_LENGTH):
            if self.board[row_i][cell_i[1]] == p and row_i != cell_i[0]:
                output = False
                break

        # Checks box
        box_i = (cell_i[0] // self.BOX_LENGTH, cell_i[1] // self.BOX_LENGTH)
        row_lbound, row_ubound = box_i[0] * self.BOX_LENGTH, (box_i[0] + 1) * self.BOX_LENGTH
        col_lbound, col_ubound = box_i[1] * self.BOX_LENGTH, (box_i[1] + 1) * self.BOX_LENGTH
        for row_i in range(row_lbound, row_ubound):
            for col_i in range(col_lbound, col_ubound):
                if self.board[row_i][col_i] == p and (row_i, col_i) != cell_i:
                    output = False
                    break
        
        return output

