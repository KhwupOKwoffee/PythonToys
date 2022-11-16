# GUI wrapper for Sudoku Solver

import tkinter as tk

from SudokuSolver import SudokuSolver


class SudokuSolverWindow(tk.Tk):

    def __init__(self):

        # Window properties
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("400x400")
        self.resizable(width = False, height = True)

        # Board string input box
        self.input = tk.StringVar(self)
        self.input_box = tk.Entry(
            self,
            width = 49,
            textvariable = self.input
        )
        self.input_box.grid(row = 0)

        # Board string output box
        self.output = tk.StringVar(self)
        self.output_box = tk.Entry(self,
            width = 49,
            textvariable = self.output,
            state = "readonly"
        )
        self.output_box.grid(row = 1)

        # Load button
        self.load_button = tk.Button(
            self,
            width = 46,
            height = 2,
            text = "Load",
            command = self.load
        )
        self.load_button.grid(row = 2)

        # Solve button
        self.solve_button = tk.Button(
            self,
            width = 46,
            height = 2,
            text = "Solve",
            command = self.solve
        )
        self.solve_button.grid(row = 3)

        # Board display & status labels
        self.board_display = tk.Label(self)
        self.board_display.grid(row = 4)
        
        self.status = tk.Label(self)
        self.status.grid(row = 5)

    def load(self):

        self.status["text"] = ""
        self.solver = SudokuSolver(board_string = self.input.get())
        self.display_board()

    def solve(self):

        self.status["text"] = "Success" if self.solver.solve() else "Failure"
        self.output.set(self.solver.get_board_string())
        self.display_board()

    def display_board(self):

        # Formats board for display in window
        text = ""
        for row_i in range(self.solver.BOARD_LENGTH):
            if row_i and not row_i % self.solver.BOX_LENGTH:
                text += "- " * round(self.solver.BOARD_LENGTH * 1.5) + "\n"
            for col_i in range(self.solver.BOARD_LENGTH):
                if col_i and not col_i % self.solver.BOX_LENGTH:
                    text += " | "
                if col_i == self.solver.BOARD_LENGTH - 1:
                    text += str(self.solver.board[row_i][col_i]) + "\n"
                else:
                    text += str(self.solver.board[row_i][col_i]) + " "
        self.board_display["text"] = text
                    
