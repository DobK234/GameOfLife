# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

from time import sleep
import tkinter as tk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

class Game_Of_Life:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Game of Life")

        win_width = 500
        win_height = 500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - win_width / 2)
        center_y = int(screen_height / 2 - win_height / 2)

        coordinates_of_window = "{}x{}+{}+{}"

        self.root.geometry(coordinates_of_window.format(win_width, win_height, center_x, center_y))
        self.root.resizable(False, False)

        self.root.attributes('-topmost', 1)

        cells = []
        for i in range(0,win_width,10):
            for j in range(0,win_height,10):
                cells.append(Cell(i,j))


class Cell:
    alive = False
    width = 10
    height = 10
    changeable = True
    x = -1
    y = -1
    dead_cell = tk.PhotoImage(file="DeadCell.png")
    alive_cell = tk.PhotoImage(file="AliveCell.png")

    def __init__(self, x, y, root):
        self.x = x
        self.y = y

        self.checkbox = tk.Button(root, command=self.check_click, text="", height=self.height, width=self.width,
                                  image=self.dead_cell,bd=0)
        self.checkbox.place(x=x, y=y)

    def check_click(self):
        if self.changeable:
            if self.alive:
                self.alive = False
                self.checkbox.configure(image=self.dead_cell)
                return
            else:
                self.alive = True
                self.checkbox.configure(image=self.alive_cell)
                return



